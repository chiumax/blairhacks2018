This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

# Stock Prophet
*The following copied from our [devpost submisstion](https://devpost.com/software/the-stock-prophet)* 

## Inspiration
We heard about Blairhacks and saw it as a great opportunity to create a solution for helping people analyze stocks and allowing them to simulate stocks.

## What it does
Our website software allows users to create their own accounts to simulate buying and selling stock shares and cryptocurrency coins.

## How we built it
We used Python Flask to program the backend and React for the frontend. We also used MongoDB as the database.

## Challenges we ran into
We ran into several challenges along the way. First, we had trouble finding a working API because both googlefinance and yahoofinance were not functional. After some additional research, we ended up using alpha_vantage (for stocks) and cryptocompare (for cryptocurrency). Also, the graphing functionality was not working, which was due to the data formatting and we managed to fix the problem.

## Accomplishments that we're proud of
We are proud that we were able to successfully get the data from the API's and correctly format it. Also, we were able to make the backend completely functional.

## What we learned
We learned how to interact with and utilize API data using both python (for back-end) and javascript (for front-end).

## What's next for The Stock Prophet
In the future, we wish to complete the frontend by making the user interface completely functional and giving the user an easy environment to simulate their buying and selling of stocks and cryptocurrencies.
