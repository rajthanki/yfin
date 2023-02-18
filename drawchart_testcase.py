import yfinance as yf
import matplotlib.pyplot as plt

import unittest
import yfinance as yf
import matplotlib.pyplot as plt

class TestStockPrice(unittest.TestCase):
    
    def test_stock_price_data(self):
        # Define the ticker symbol
        tickerSymbol = 'RELIANCE.NS'

        # Get data for the ticker
        tickerData = yf.Ticker(tickerSymbol)

        # Get the historical prices for this ticker
        tickerDf = tickerData.history(period='1d', start='2022-01-01', end='2022-02-01')

        # Check that the ticker data is not empty
        self.assertFalse(tickerDf.empty, "Ticker data is empty")

        # Check that the data contains the expected columns
        self.assertIn('Close', tickerDf.columns, "Close column not found")
        self.assertIn('Open', tickerDf.columns, "Open column not found")
        self.assertIn('High', tickerDf.columns, "High column not found")
        self.assertIn('Low', tickerDf.columns, "Low column not found")

        # Check that the date range is correct
        self.assertEqual(tickerDf.index[0].date(), datetime.date(2022, 1, 3), "Start date is incorrect")
        self.assertEqual(tickerDf.index[-1].date(), datetime.date(2022, 1, 31), "End date is incorrect")
        
        # Check that the closing price data is valid
        self.assertTrue(tickerDf['Close'].isnull().sum() == 0, "Close price data contains NaN values")
        self.assertTrue(tickerDf['Close'].min() > 0, "Close price data contains invalid values")

    def test_stock_price_chart(self):
        # Define the ticker symbol
        tickerSymbol = 'RELIANCE.NS'

        # Get data for the ticker
        tickerData = yf.Ticker(tickerSymbol)

        # Get the historical prices for this ticker
        tickerDf = tickerData.history(period='1d', start='2022-01-01', end='2022-02-01')

        # Create a line chart
        plt.plot(tickerDf['Close'])

        # Add a title and axis labels
        plt.title('Reliance Industries Stock Price')
        plt.xlabel('Date')
        plt.ylabel('Closing Price (INR)')

        # Check that the chart was created successfully
        self.assertIsNotNone(plt.gca().lines, "Chart was not created")

        # Check that the chart displays the expected data
        self.assertEqual(plt.gca().lines[0].get_xdata()[0].date(), datetime.date(2022, 1, 3), "Start date is incorrect")
        self.assertEqual(plt.gca().lines[0].get_xdata()[-1].date(), datetime.date(2022, 1, 31), "End date is incorrect")
        self.assertEqual(plt.gca().lines[0].get_ydata()[0], tickerDf['Close'][0], "Starting price is incorrect")
        self.assertEqual(plt.gca().lines[0].get_ydata()[-1], tickerDf['Close'][-1], "Ending price is incorrect")
