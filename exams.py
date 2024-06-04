import random
from fpdf import FPDF


def generate_exam(questions, answers):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.add_font("DejaVu", "", "DejaVuSansCondensed.ttf")
    pdf.set_font("DejaVu", size=12)

    for i, question in enumerate(questions):
        if not isinstance(question['options'], dict):
            raise TypeError(
                f"Expected a dictionary for options, but got {type(question['options'])} for question {i + 1}")
        pdf.multi_cell(25, 10, f"Q{i + 1}: {question['question']}", 1, 'L', 1)
        for key, option in question['options'].items():
            pdf.multi_cell(25, 10, f"    {key}: {option}")

    pdf.add_page()
    pdf.multi_cell(200, 10, f"Q{i + 1}: {question['question']}", 1, 'L', 0)
    for i, answer in enumerate(answers):
        pdf.multi_cell(25, 10, f"Q{i + 1}: {answer}", 0, 'L')

    return pdf


# List of questions
questions = [
    {
        "question": "Different firm types (legal forms) were studied during the course. Which statement on these legal forms is FALSE?",
        "options": {
            "A": "Private equity funds and venture capital funds are two examples of industries dominated by limited partnerships.",
            "B": "In a partnership it can be that some partners only have limited liability.",
            "C": "Partnerships are the least common type of firm.",
            "D": "In a sole proprietorship the owner has limited personal liability for any of the firm's debts."
        },
        "answer": "D"
    },
    {
        "question": "You agreed with your bank on a 25-year mortgage loan with quarterly payments of €2,500 and a quarterly interest rate of 0.25%. The present value of the loan comes closest to:",
        "options": {
            "A": "€215,000",
            "B": "€217,000",
            "C": "€219,000",
            "D": "€221,000"
        },
        "answer": "D"
    },
    {
        "question": "The government issued a perpetual bond that promises an annual interest payment of $10 to the holder. The current yield to maturity is 6%. Assuming the yield to maturity remains constant over time, the price of the bond immediately before the first interest payment is made comes closest to:",
        "options": {
            "A": "$19",
            "B": "$9",
            "C": "$177",
            "D": "$167"
        },
        "answer": "C"
    },
    {
        "question": "Assume the Capital Asset Pricing Model (CAPM) applies. The expected return on the market portfolio is 10% and the expected return on individual stock Coinbazar is 5%. The risk-free rate is 3%. The beta of stock Coinbazar comes closest to:",
        "options": {
            "A": "0.2",
            "B": "0.285",
            "C": "3.5",
            "D": "3.75"
        },
        "answer": "B"
    },
    {
        "question": "Which statement about corporate bankruptcy is FALSE?",
        "options": {
            "A": "Corporate bankruptcy cannot arise in corporations without debt/loans.",
            "B": "Corporate bankruptcy implies a transfer of ownership and control from the shareholders to the debtholders.",
            "C": "Corporate bankruptcy automatically implies a liquidation of the corporation.",
            "D": "Corporate bankruptcy arises when corporations cannot fulfill their debt obligations to their debtholders (bondholders, banks)."
        },
        "answer": "C"
    },
    {
        "question": "Suppose you save €1,000 per year and this for 30 consecutive years. If the account earns 6% interest per year, the future value of the savings account (after 30 years) comes closest to:",
        "options": {
            "A": "€75,000",
            "B": "€80,000",
            "C": "€85,000",
            "D": "€90,000"
        },
        "answer": "B"
    },
    {
        "question": "Consider two bonds simultaneously issued by the same government: a 25-year coupon bond and a 30-year coupon bond with common face value of $1,000. Both bonds have a coupon rate of 5%. Moreover, both bonds exhibit the same yield to maturity of 4%. Which statement is FALSE?",
        "options": {
            "A": "Both bonds trade at a premium (above par).",
            "B": "The 30-year bond exhibits more interest rate risk than the 25-year bond.",
            "C": "The 30-year bond is cheaper than the 25-year bond.",
            "D": "A 1% increase in their yield to maturity from 4% to 5% would result in a larger price decrease for the 30-year bond as compared to the 25-year bond."
        },
        "answer": "C"
    },
    {
        "question": "Consider two bonds simultaneously issued by the same government: a 25-year coupon bond and a 30-year coupon bond with common face value of $1,000. Both bonds have a coupon rate of 5%. Moreover, both bonds exhibit the same yield to maturity of 4%. Which statement is FALSE?",
        "options": {
            "A": "Both bonds trade at a premium (above par).",
            "B": "The 30-year bond exhibits more interest rate risk than the 25-year bond.",
            "C": "The 30-year bond is cheaper than the 25-year bond.",
            "D": "A 1% increase in their yield to maturity from 4% to 5% would result in a larger price decrease for the 30-year bond as compared to the 25-year bond."
        },
        "answer": "C"
    },
    {
        "question": "Consider portfolios P consisting of two stocks only. The stock with the highest expected return also exhibits the highest standard deviation. We are interested in plotting the expected portfolio return (vertical axis) against the portfolio standard deviation (horizontal axis) for each possible 2-stock portfolio. Which statement is FALSE?",
        "options": {
            "A": "This curve can contain both efficient and inefficient portfolios.",
            "B": "The portfolio variance decreases when the correlation between the two stocks decreases (keeping all other determinants of the portfolio variance constant).",
            "C": "A (2-stock) portfolio is efficient when no other (2-stock) portfolios can be found with equal expected return but with lower standard deviation.",
            "D": "When plotting expected portfolio returns vs. portfolio volatility the curve that contains all possible portfolios is a straight line if and only if the correlation between the two stocks is 0."
        },
        "answer": "D"
    },
    {
        "question": "Assume investors only trade on public information that is easy to interpret. Which of the following statements related to the processing of information in market prices and the efficient markets hypothesis is FALSE?",
        "options": {
            "A": "In efficient markets, investors expect the same returns for different stocks because otherwise this would represent an arbitrage opportunity.",
            "B": "In efficient markets, all past publically available information relevant for a stock cannot cause changes in the current stock price.",
            "C": "In efficient markets, it is possible that the announcement of a merger does not impact the stock price of the target and the acquirer.",
            "D": "In efficient markets, you expect that the Net Present Value of a financial investment will be equal to zero."
        },
        "answer": "A"
    },
    {
        "question": "Which statement on an investment's Internal Rate of Return (IRR) is FALSE?",
        "options": {
            "A": "In contrast to a zero-coupon bond's IRR, a coupon bond's IRR cannot be calculated using a simple formula.",
            "B": "The IRR 'investment rule' states that one needs to take any investment opportunity when the IRR exceeds the opportunity cost of capital.",
            "C": "A coupon bond's IRR is equal to its coupon interest rate (regardless the level of the yield to maturity).",
            "D": "An investment project's IRR is the discount rate that sets the Net Present Value of a project's cash flows equal to zero."
        },
        "answer": "C"
    },
    {
        "question": "We considered various ways to value company equity. Which of the following statements is TRUE?",
        "options": {
            "A": "The dividend discount model can only be used when dividends have a constant growth rate.",
            "B": "The total pay out model can only be used when share repurchases are nonzero in magnitude.",
            "C": "The discounted free cash flow model uses the firm's equity cost of capital as relevant discount rate.",
            "D": "Contrary to the dividend discount model, one needs to know the amount of shares outstanding when implementing the total pay out and discounted free cash flow models to determine a stock's intrinsic value."
        },
        "answer": "D"
    },
    {
        "question": "Consider an equally weighted portfolio that contains 10 stocks. If the average standard deviation of these stocks is 40% and the average correlation between the stocks is 25%, then the standard deviation of this equally weighted portfolio is closest to:",
        "options": {
            "A": "19.2%",
            "B": "5.76%",
            "C": "24%",
            "D": "30%"
        },
        "answer": "C"
    },
    {
        "question": "A lot of accounting terms related to a corporation's financial statements are used by financial analysts. Which statement is FALSE?",
        "options": {
            "A": "The book value of the firm's assets can fall below the book value of the firm's liabilities.",
            "B": "A rise in goodwill (all else equal on the balance sheet) leads to an increase in book value of equity.",
            "C": "One of the steps to calculate net income in the income statement is to add interest income to Earnings Before Interest and Taxes (EBIT).",
            "D": "The diluted Earnings per share are not calculated by using the actual number of outstanding shares."
        },
        "answer": "C"
    },
    {
        "question": "Which asset class historically shows the highest risk premium?",
        "options": {
            "A": "Large stocks.",
            "B": "Corporate bonds.",
            "C": "Treasury Bills.",
            "D": "Small stocks."
        },
        "answer": "D"
    },
    {
        "question": "A stock of company Notax was worth $20 on December 31, 2020 whereas it is expected to rise to $40 on December 31, 2021. Notax is paying a dividend per share of $4 over 2021. Assume constant dividend growth in the future. Which statement is FALSE?",
        "options": {
            "A": "The total (expected) stock return over 2021 equals 120%.",
            "B": "The constant growth rate of dividends over 2021 equals 70%",
            "C": "The expected capital gain rate over 2021 equals 100%.",
            "D": "The 2021 dividend yield equals 20%."
        },
        "answer": "B"
    },
    {
        "question": "Assume the Capital Asset Pricing Model (CAPM) applies. Stock Purple's expected return is 8.25% whereas stock Violet's expected return equals 11.75%. If the risk-free rate is 3% and the expected return on the market portfolio is 10%, then the beta of a portfolio that consists of 40% Purple stock and 60% Violet stock is closest to:",
        "options": {
            "A": "0.75",
            "B": "1.25",
            "C": "1.05",
            "D": "1.35"
        },
        "answer": "C"
    },
    {
        "question": "You overhear your manager saying that she plans to book an Ocean-view room on her upcoming trip to Miami for a meeting. You know that the interior rooms are much less expensive, but that your manager is traveling at the Company's expense. This use of additional funds comes about as a result of:",
        "options": {
            "A": "an agency problem.",
            "B": "an adverse selection problem.",
            "C": "a moral hazard.",
            "D": "a publicity problem."
        },
        "answer": "A"
    },
    {
        "question": "An agency problem can be alleviated by:",
        "options": {
            "A": "requiring all firms to be sole proprietorships.",
            "B": "compensating managers in such a way that acting in the best interest of shareholders is also in the best interest of managers.",
            "C": "asking managers to take on more risk than they are comfortable taking.",
            "D": "A and B."
        },
        "answer": "D"
    },
    {
        "question": "Which of the following are subject to double taxation?",
        "options": {
            "A": "Corporation",
            "B": "Partnership",
            "C": "Sole proprietorship",
            "D": "A and B"
        },
        "answer": "A"
    },
    {
        "question": "The largest stock market in the world is",
        "options": {
            "A": "the London Stock Exchange.",
            "B": "NASDAQ.",
            "C": "the American Stock Exchange.",
            "D": "the New York Stock Exchange."
        },
        "answer": "D"
    },
    {
        "question": "An investment is said to be liquid if the investment",
        "options": {
            "A": "has large day to day fluctuations in price.",
            "B": "has a large bid-ask spread.",
            "C": "can easily be converted into cash.",
            "D": "is traded on a stock exchange."
        },
        "answer": "C"
    },
    {
        "question": "What type of company trades on an organized stock exchange?",
        "options": {
            "A": "A limited liability company",
            "B": "A private company",
            "C": "An 'S' corporation",
            "D": "A public company"
        },
        "answer": "D"
    },
    {
        "question": "Which of the following statements is false?",
        "options": {
            "A": "On Nasdaq, stocks can and do have multiple market makers who compete with each other. Each market maker must post bid and ask prices in the Nasdaq network where they can be viewed by all participants.",
            "B": "Bid prices exceed ask prices.",
            "C": "Because customers always buy at the ask and sell at the bid, the bid-ask spread is a transaction cost investors have to pay in order to trade.",
            "D": "On the floor of the NYSE, market makers (known on the NYSE as specialists) match buyers and sellers."
        },
        "answer": "B"
    },
    {
        "question": "If you buy shares of Coca-Cola on the primary market,",
        "options": {
            "A": "Coca-Cola receives the money because the company has issued new shares.",
            "B": "you buy the shares from another investor who decided to sell the shares.",
            "C": "you buy the shares from the New York Stock Exchange.",
            "D": "you buy the shares from the Federal Reserve."
        },
        "answer": "A"
    },
    {
        "question": "If you buy shares of Coca-Cola on the secondary market,",
        "options": {
            "A": "Coca-Cola receives the money because the company has issued new shares.",
            "B": "you buy the shares from another investor who decided to sell the shares.",
            "C": "you buy the shares from the New York Stock Exchange.",
            "D": "you buy the shares from the Federal Reserve."
        },
        "answer": "B"
    },
    {
        "question": "Which of the following statements regarding the income statement is incorrect?",
        "options": {
            "A": "The income statement shows the earnings and expenses at a given point in time.",
            "B": "The income statement shows the flow of earnings and expenses generated by the firm between two dates.",
            "C": "The last or 'bottom' line of the income statement shows the firm's net income.",
            "D": "The first line of an income statement lists the revenues from the sales of products or services."
        },
        "answer": "A"
    },
    {
        "question": "Gross profit is calculated as:",
        "options": {
            "A": "Total sales - cost of sales - selling, general and administrative expenses - depreciation and amortization",
            "B": "Total sales - cost of sales - selling, general and administrative expenses",
            "C": "Total sales - cost of sales",
            "D": "None of the above"
        },
        "answer": "C"
    },
    {
        "question": "Which of the following is not an operating expense?",
        "options": {
            "A": "Interest expense",
            "B": "Depreciation and amortization",
            "C": "Selling, general and administrative expenses",
            "D": "Research and development"
        },
        "answer": "A"
    },
    {
        "question": "The firm's revenues and expenses over a period of time are reported on the firm's",
        "options": {
            "A": "income statement or statement of financial performance.",
            "B": "income statement or statement of financial position.",
            "C": "balance sheet or statement of financial performance.",
            "D": "balance sheet or statement of financial position."
        },
        "answer": "A"
    },
    {
        "question": "The statement of financial performance is also known as the",
        "options": {
            "A": "balance sheet.",
            "B": "income statement.",
            "C": "statement of cash flows.",
            "D": "statement of stockholder's equity."
        },
        "answer": "B"
    },
    {
        "question": "U.S. public companies are required to file their annual financial statements with the U.S. Securities and Exchange Commission on which form?",
        "options": {
            "A": "10-A",
            "B": "10-K",
            "C": "10-Q",
            "D": "10-SEC"
        },
        "answer": "B"
    },
    {
        "question": "Which of the following is not a financial statement that every public company is required to produce?",
        "options": {
            "A": "Income Statement",
            "B": "Statement of Sources and Uses of Cash",
            "C": "Balance Sheet",
            "D": "Statement of Stockholders' Equity"
        },
        "answer": "B"
    },
    {
        "question": "The third party who checks annual financial statements to ensure that they are prepared according to GAAP and verifies that the information reported is reliable is the",
        "options": {
            "A": "NYSE Enforcement Board.",
            "B": "Accounting Standards Board.",
            "C": "Securities and Exchange Commission (SEC).",
            "D": "auditor."
        },
        "answer": "D"
    },
    {
        "question": "Which of the following balance sheet equations is incorrect?",
        "options": {
            "A": "Assets - Liabilities = Shareholders' Equity",
            "B": "Assets = Liabilities + Shareholders' Equity",
            "C": "Assets - Current Liabilities = Long Term Liabilities",
            "D": "Assets - Current Liabilities = Long Term Liabilities + Shareholders' Equity"
        },
        "answer": "C"
    },
    {
        "question": "Cash is a",
        "options": {
            "A": "Long-term Asset.",
            "B": "Current Asset.",
            "C": "Current Liability.",
            "D": "Long-term Liability."
        },
        "answer": "B"
    },
    {
        "question": "Accounts payable is a",
        "options": {
            "A": "Long-term Liability.",
            "B": "Current Asset.",
            "C": "Long-term Asset.",
            "D": "Current Liability."
        },
        "answer": "D"
    },
    {
        "question": "A 30 year mortgage loan is a",
        "options": {
            "A": "Long-term Liability.",
            "B": "Current Liability.",
            "C": "Current Asset.",
            "D": "Long-term Asset."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following statements regarding the balance sheet is incorrect?",
        "options": {
            "A": "The balance sheet provides a snapshots of the firm's financial position at a given point in time.",
            "B": "The balance sheet lists the firm's assets and liabilities.",
            "C": "The balance sheet reports stockholders' equity on the right-hand side.",
            "D": "The balance sheet reports liabilities on the left-hand side."
        },
        "answer": "D"
    },
    {
        "question": "Dustin's Donuts experienced a decrease in the value of the trademark of a company it acquired two years ago. This reduction in value results in",
        "options": {
            "A": "an impairment charge.",
            "B": "depreciation expense.",
            "C": "an operating expense.",
            "D": "goodwill."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following is an example of an intangible asset?",
        "options": {
            "A": "Brand names and trademarks",
            "B": "Patents",
            "C": "Customer relationships",
            "D": "All of the above are intangible assets."
        },
        "answer": "D"
    },
    {
        "question": "On the balance sheet, short-term debt appears",
        "options": {
            "A": "in the Stockholders' Equity section.",
            "B": "in the Operating Expenses section.",
            "C": "in the Current Assets section.",
            "D": "in the Current Liabilities section."
        },
        "answer": "D"
    },
    {
        "question": "On the balance sheet, current maturities of long-term debt appear",
        "options": {
            "A": "in the Stockholders' Equity section.",
            "B": "in the Operating Expenses section.",
            "C": "in the Current Assets section.",
            "D": "in the Current Liabilities section."
        },
        "answer": "D"
    },
    {
        "question": "The firm's assets and liabilities at a given point in time are reported on the firm's",
        "options": {
            "A": "income statement or statement of financial performance.",
            "B": "income statement or statement of financial position.",
            "C": "balance sheet or statement of financial performance.",
            "D": "balance sheet or statement of financial position."
        },
        "answer": "D"
    },
    {
        "question": "The statement of financial position is also known as the",
        "options": {
            "A": "balance sheet.",
            "B": "income statement.",
            "C": "statement of cash flows.",
            "D": "statement of stockholder's equity."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following is not a reason why cash flow may not equal net income?",
        "options": {
            "A": "Amortization is added in when calculating net income.",
            "B": "Changes in inventory will change cash flows but not income.",
            "C": "Capital expenditures are not recorded on the income statement.",
            "D": "Depreciation is deducted when calculating net income."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following adjustments to net income is not correct if you are trying to calculate cash flow from operating activities?",
        "options": {
            "A": "Add increases in accounts payable",
            "B": "Add back depreciation",
            "C": "Add increases in accounts receivable",
            "D": "Deduct increases in inventory"
        },
        "answer": "C"
    },
    {
        "question": "Which of the following adjustments is not correct if you are trying to calculate cash flow from financing activities?",
        "options": {
            "A": "Add dividends paid",
            "B": "Add any increase in long term borrowing",
            "C": "Add any increase in short-term borrowing",
            "D": "Add proceeds from the sale of stock"
        },
        "answer": "A"
    },
    {
        "question": "In addition to the balance sheet, income statement, and the statement of cash flows, a firm's complete financial statements will include all of the following except:",
        "options": {
            "A": "Management discussion and Analysis",
            "B": "Notes to the financial statements",
            "C": "Securities and Exchange Commission's (SEC) commentary",
            "D": "Statement of stockholders' equity"
        },
        "answer": "C"
    },
    {
        "question": "Off-balance sheet transactions are required to be disclosed",
        "options": {
            "A": "in the management discussion and analysis.",
            "B": "in the auditor's report.",
            "C": "in the Securities and Exchange Commission's commentary.",
            "D": "in the statement of stockholders' equity."
        },
        "answer": "A"
    },
    {
        "question": "Details of acquisitions, spin-offs, leases, taxes, and risk management activities are given",
        "options": {
            "A": "in the management discussion and analysis.",
            "B": "in the Securities and Exchange Commission's commentary.",
            "C": "in the auditor's report.",
            "D": "in the notes to the financial statements."
        },
        "answer": "D"
    },
    {
        "question": "The Sarbanes-Oxley Act (SOX) was passed by Congress in 2002, in response to",
        "options": {
            "A": "financial scandals, including WorldCom and Enron.",
            "B": "financial scandals, including Bernie Madoff and AIG.",
            "C": "financial scandals, including General Motors and Chrysler.",
            "D": "the Troubled Asset Relief Program (TARP)."
        },
        "answer": "A"
    },

    {
        "question": "Which of the following statements is false?",
        "options": {
            "A": "In bankruptcy, management is given the opportunity to reorganize the firm and renegotiate with debt holders.",
            "B": "Because a corporation is a separate legal entity, when it fails to repay its debts, the people who lent to the firm, the debt holders, are entitled to seize the assets of the corporation in compensation for the default.",
            "C": "As long as the corporation can satisfy the claims of the debt holders, ownership remains in the hands of the equity holders.",
            "D": "If the corporation fails to satisfy debt holders' claims, debt holders may lose control of the firm."
        },
        "answer": "D"
    },
    {
        "question": "Which of the following are subject to double taxation?",
        "options": {
            "A": "Corporation",
            "B": "Partnership",
            "C": "Sole proprietorship",
            "D": "A and B"
        },
        "answer": "A"
    },
    {
        "question": "You own 100 shares of a 'C' Corporation. The corporation earns $5.00 per share before taxes. Once the corporation has paid any corporate taxes that are due, it will distribute the rest of its earnings to its shareholders in the form of a dividend. If the corporate tax rate is 40% and your personal tax rate on (both dividend and non-dividend) income is 30%, then how much money is left for you after all taxes have been paid?",
        "options": {
            "A": "$210",
            "B": "$300",
            "C": "$350",
            "D": "$500"
        },
        "answer": "A"
    },
    {
        "question": "You own 100 shares of a Sub Chapter 'S' Corporation. The corporation earns $5.00 per share before taxes. Once the corporation has paid any corporate taxes that are due, it will distribute the rest of its earnings to its shareholders in the form of a dividend. If the corporate tax rate is 40% and your personal tax rate on (both dividend and non-dividend) income is 30%, then how much money is left for you after all taxes have been paid?",
        "options": {
            "A": "$210",
            "B": "$300",
            "C": "$350",
            "D": "$500"
        },
        "answer": "C"
    },
    {
        "question": "In a corporation, the ultimate decisions regarding business matters are made by",
        "options": {
            "A": "the Board of Directors",
            "B": "debt holders",
            "C": "shareholders",
            "D": "investors"
        },
        "answer": "A"
    },
    {
        "question": "The person charged with running the corporation by instituting the rules and policies set by the board of directors is called",
        "options": {
            "A": "the Chief Operating Officer",
            "B": "the Company President",
            "C": "the Chief Executive Officer",
            "D": "the Chief Financial Officer"
        },
        "answer": "C"
    },
    {
        "question": "The Principal-Agent Problem arises",
        "options": {
            "A": "because managers have little incentive to work in the interest of shareholders when this means working against their own self-interest.",
            "B": "because of the separation of ownership and control in a corporation.",
            "C": "Both A and B",
            "D": "None of the above"
        },
        "answer": "C"
    },
    {
        "question": "If shareholders are unhappy with a CEO's performance, they are most likely to",
        "options": {
            "A": "buy more shares in an effort to gain control of the firm.",
            "B": "file a shareholder resolution.",
            "C": "replace the CEO through a grassroots shareholder uprising.",
            "D": "sell their shares."
        },
        "answer": "D"
    },
    {
        "question": "A ________ is when a rich individual or organization purchases a large fraction of the stock of a poorly performing firm and in doing so gets enough votes to replace the board of directors and the CEO.",
        "options": {
            "A": "shareholder proposal",
            "B": "leveraged buyout",
            "C": "shareholder action",
            "D": "hostile takeover"
        },
        "answer": "D"
    },
    {
        "question": "The most senior financial manager in a corporation is usually called:",
        "options": {
            "A": "the chief executive officer.",
            "B": "the chief financial officer.",
            "C": "the chief operating officer.",
            "D": "the chairman of the board."
        },
        "answer": "B"
    },
    {
        "question": "You overhear your manager saying that she plans to book an Ocean-view room on her upcoming trip to Miami for a meeting. You know that the interior rooms are much less expensive, but that your manager is traveling at the Company's expense. This use of additional funds comes about as a result of:",
        "options": {
            "A": "an agency problem.",
            "B": "an adverse selection problem.",
            "C": "a moral hazard.",
            "D": "a publicity problem."
        },
        "answer": "A"
    },
    {
        "question": "An agency problem can be alleviated by:",
        "options": {
            "A": "requiring all firms to be sole proprietorships.",
            "B": "compensating managers in such a way that acting in the best interest of shareholders is also in the best interest of managers.",
            "C": "asking managers to take on more risk than they are comfortable taking.",
            "D": "A and B."
        },
        "answer": "D"
    },
    {
        "question": "Which of the following statements regarding limited partnerships is true?",
        "options": {
            "A": "There is no limit on a limited partner's liability.",
            "B": "A limited partner's liability is limited by the amount of their investment.",
            "C": "A limited partner is not liable until all the assets of the general partners have been exhausted.",
            "D": "A general partner's liability is limited by the amount of their investment."
        },
        "answer": "B"
    },
    {
        "question": "Which of the following is an advantage of incorporation?",
        "options": {
            "A": "Access to capital markets",
            "B": "Limited liability",
            "C": "Unlimited life",
            "D": "All of the above"
        },
        "answer": "D"
    },
    {
        "question": "Which of the following statements is most correct?",
        "options": {
            "A": "An advantage to incorporation is that it allows for less regulation of the business.",
            "B": "An advantage of a corporation is that it is subject to double taxation.",
            "C": "Unlike a partnership, a disadvantage of a corporation is that it has limited liability.",
            "D": "Corporations face more regulations when compared to partnerships."
        },
        "answer": "D"
    },
    {
        "question": "A limited liability company is essentially",
        "options": {
            "A": "a limited partnership without limited partners.",
            "B": "a limited partnership without a general partner.",
            "C": "just another name for a limited partnership.",
            "D": "just another name for a corporation."
        },
        "answer": "B"
    },
    {
        "question": "The distinguishing feature of a corporation is that",
        "options": {
            "A": "there is no legal difference between the corporation and its owners.",
            "B": "it is a legally defined, artificial being, separate from its owners.",
            "C": "it spreads liability for its corporate obligations to all shareholders.",
            "D": "it provides limited liability only to small shareholders."
        },
        "answer": "B"
    },
    {
        "question": "Which of the following balance sheet equations is incorrect?",
        "options": {
            "A": "Assets - Liabilities = Shareholders' Equity",
            "B": "Assets = Liabilities + Shareholders' Equity",
            "C": "Assets - Current Liabilities = Long Term Liabilities",
            "D": "Assets - Current Liabilities = Long Term Liabilities + Shareholders' Equity"
        },
        "answer": "C"
    },
    {
        "question": "Cash is a",
        "options": {
            "A": "Long-term Asset.",
            "B": "Current Asset.",
            "C": "Current Liability.",
            "D": "Long-term Liability."
        },
        "answer": "B"
    },
    {
        "question": "Accounts payable is a",
        "options": {
            "A": "Long-term Liability.",
            "B": "Current Asset.",
            "C": "Long-term Asset.",
            "D": "Current Liability."
        },
        "answer": "D"
    },
    {
        "question": "A 30 year mortgage loan is a",
        "options": {
            "A": "Long-term Liability.",
            "B": "Current Liability.",
            "C": "Current Asset.",
            "D": "Long-term Asset."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following statements regarding the balance sheet is incorrect?",
        "options": {
            "A": "The balance sheet provides a snapshots of the firm's financial position at a given point in time.",
            "B": "The balance sheet lists the firm's assets and liabilities.",
            "C": "The balance sheet reports stockholders' equity on the right-hand side.",
            "D": "The balance sheet reports liabilities on the left-hand side."
        },
        "answer": "D"
    },
    {
        "question": "Dustin's Donuts experienced a decrease in the value of the trademark of a company it acquired two years ago. This reduction in value results in",
        "options": {
            "A": "an impairment charge.",
            "B": "depreciation expense.",
            "C": "an operating expense.",
            "D": "goodwill."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following is an example of an intangible asset?",
        "options": {
            "A": "Brand names and trademarks",
            "B": "Patents",
            "C": "Customer relationships",
            "D": "All of the above are intangible assets."
        },
        "answer": "D"
    },
    {
        "question": "On the balance sheet, short-term debt appears",
        "options": {
            "A": "in the Stockholders' Equity section.",
            "B": "in the Operating Expenses section.",
            "C": "in the Current Assets section.",
            "D": "in the Current Liabilities section."
        },
        "answer": "D"
    },
    {
        "question": "On the balance sheet, current maturities of long-term debt appear",
        "options": {
            "A": "in the Stockholders' Equity section.",
            "B": "in the Operating Expenses section.",
            "C": "in the Current Assets section.",
            "D": "in the Current Liabilities section."
        },
        "answer": "D"
    },
    {
        "question": "The firm's assets and liabilities at a given point in time are reported on the firm's",
        "options": {
            "A": "income statement or statement of financial performance.",
            "B": "income statement or statement of financial position.",
            "C": "balance sheet or statement of financial performance.",
            "D": "balance sheet or statement of financial position."
        },
        "answer": "D"
    },
    {
        "question": "The statement of financial position is also known as the",
        "options": {
            "A": "balance sheet.",
            "B": "income statement.",
            "C": "statement of cash flows.",
            "D": "statement of stockholder's equity."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following is not a reason why cash flow may not equal net income?",
        "options": {
            "A": "Amortization is added in when calculating net income.",
            "B": "Changes in inventory will change cash flows but not income.",
            "C": "Capital expenditures are not recorded on the income statement.",
            "D": "Depreciation is deducted when calculating net income."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following adjustments to net income is not correct if you are trying to calculate cash flow from operating activities?",
        "options": {
            "A": "Add increases in accounts payable",
            "B": "Add back depreciation",
            "C": "Add increases in accounts receivable",
            "D": "Deduct increases in inventory"
        },
        "answer": "C"
    },
    {
        "question": "Which of the following adjustments is not correct if you are trying to calculate cash flow from financing activities?",
        "options": {
            "A": "Add dividends paid",
            "B": "Add any increase in long term borrowing",
            "C": "Add any increase in short-term borrowing",
            "D": "Add proceeds from the sale of stock"
        },
        "answer": "A"
    },
    {
        "question": "In addition to the balance sheet, income statement, and the statement of cash flows, a firm's complete financial statements will include all of the following except:",
        "options": {
            "A": "Management discussion and Analysis",
            "B": "Notes to the financial statements",
            "C": "Securities and Exchange Commission's (SEC) commentary",
            "D": "Statement of stockholders' equity"
        },
        "answer": "C"
    },
    {
        "question": "Off-balance sheet transactions are required to be disclosed",
        "options": {
            "A": "in the management discussion and analysis.",
            "B": "in the auditor's report.",
            "C": "in the Securities and Exchange Commission's commentary.",
            "D": "in the statement of stockholders' equity."
        },
        "answer": "A"
    },
    {
        "question": "Details of acquisitions, spin-offs, leases, taxes, and risk management activities are given",
        "options": {
            "A": "in the management discussion and analysis.",
            "B": "in the Securities and Exchange Commission's commentary.",
            "C": "in the auditor's report.",
            "D": "in the notes to the financial statements."
        },
        "answer": "D"
    },
    {
        "question": "The Sarbanes-Oxley Act (SOX) was passed by Congress in 2002, in response to",
        "options": {
            "A": "financial scandals, including WorldCom and Enron.",
            "B": "financial scandals, including Bernie Madoff and AIG.",
            "C": "financial scandals, including General Motors and Chrysler.",
            "D": "the Troubled Asset Relief Program (TARP)."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following is not a financial statement that every public company is required to produce?",
        "options": {
            "A": "Income Statement",
            "B": "Statement of Sources and Uses of Cash",
            "C": "Balance Sheet",
            "D": "Statement of Stockholders' Equity"
        },
        "answer": "B"
    },
    {
        "question": "The third party who checks annual financial statements to ensure that they are prepared according to GAAP and verifies that the information reported is reliable is the",
        "options": {
            "A": "NYSE Enforcement Board.",
            "B": "Accounting Standards Board.",
            "C": "Securities and Exchange Commission (SEC).",
            "D": "auditor."
        },
        "answer": "D"
    },
    {
        "question": "Which of the following balance sheet equations is incorrect?",
        "options": {
            "A": "Assets - Liabilities = Shareholders' Equity",
            "B": "Assets = Liabilities + Shareholders' Equity",
            "C": "Assets - Current Liabilities = Long Term Liabilities",
            "D": "Assets - Current Liabilities = Long Term Liabilities + Shareholders' Equity"
        },
        "answer": "C"
    },
    {
        "question": "Cash is a",
        "options": {
            "A": "Long-term Asset.",
            "B": "Current Asset.",
            "C": "Current Liability.",
            "D": "Long-term Liability."
        },
        "answer": "B"
    },
    {
        "question": "Accounts payable is a",
        "options": {
            "A": "Long-term Liability.",
            "B": "Current Asset.",
            "C": "Long-term Asset.",
            "D": "Current Liability."
        },
        "answer": "D"
    },
    {
        "question": "A 30 year mortgage loan is a",
        "options": {
            "A": "Long-term Liability.",
            "B": "Current Liability.",
            "C": "Current Asset.",
            "D": "Long-term Asset."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following statements regarding the balance sheet is incorrect?",
        "options": {
            "A": "The balance sheet provides a snapshots of the firm's financial position at a given point in time.",
            "B": "The balance sheet lists the firm's assets and liabilities.",
            "C": "The balance sheet reports stockholders' equity on the right-hand side.",
            "D": "The balance sheet reports liabilities on the left-hand side."
        },
        "answer": "D"
    },
    {
        "question": "Dustin's Donuts experienced a decrease in the value of the trademark of a company it acquired two years ago. This reduction in value results in",
        "options": {
            "A": "an impairment charge.",
            "B": "depreciation expense.",
            "C": "an operating expense.",
            "D": "goodwill."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following is an example of an intangible asset?",
        "options": {
            "A": "Brand names and trademarks",
            "B": "Patents",
            "C": "Customer relationships",
            "D": "All of the above are intangible assets."
        },
        "answer": "D"
    },
    {
        "question": "On the balance sheet, short-term debt appears",
        "options": {
            "A": "in the Stockholders' Equity section.",
            "B": "in the Operating Expenses section.",
            "C": "in the Current Assets section.",
            "D": "in the Current Liabilities section."
        },
        "answer": "D"
    },
    {
        "question": "On the balance sheet, current maturities of long-term debt appear",
        "options": {
            "A": "in the Stockholders' Equity section.",
            "B": "in the Operating Expenses section.",
            "C": "in the Current Assets section.",
            "D": "in the Current Liabilities section."
        },
        "answer": "D"
    },
    {
        "question": "The firm's assets and liabilities at a given point in time are reported on the firm's",
        "options": {
            "A": "income statement or statement of financial performance.",
            "B": "income statement or statement of financial position.",
            "C": "balance sheet or statement of financial performance.",
            "D": "balance sheet or statement of financial position."
        },
        "answer": "D"
    },
    {
        "question": "The statement of financial position is also known as the",
        "options": {
            "A": "balance sheet.",
            "B": "income statement.",
            "C": "statement of cash flows.",
            "D": "statement of stockholder's equity."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following is not a reason why cash flow may not equal net income?",
        "options": {
            "A": "Amortization is added in when calculating net income.",
            "B": "Changes in inventory will change cash flows but not income.",
            "C": "Capital expenditures are not recorded on the income statement.",
            "D": "Depreciation is deducted when calculating net income."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following adjustments to net income is not correct if you are trying to calculate cash flow from operating activities?",
        "options": {
            "A": "Add increases in accounts payable",
            "B": "Add back depreciation",
            "C": "Add increases in accounts receivable",
            "D": "Deduct increases in inventory"
        },
        "answer": "C"
    },
    {
        "question": "Which of the following adjustments is not correct if you are trying to calculate cash flow from financing activities?",
        "options": {
            "A": "Add dividends paid",
            "B": "Add any increase in long term borrowing",
            "C": "Add any increase in short-term borrowing",
            "D": "Add proceeds from the sale of stock"
        },
        "answer": "A"
    },
    {
        "question": "In addition to the balance sheet, income statement, and the statement of cash flows, a firm's complete financial statements will include all of the following except:",
        "options": {
            "A": "Management discussion and Analysis",
            "B": "Notes to the financial statements",
            "C": "Securities and Exchange Commission's (SEC) commentary",
            "D": "Statement of stockholders' equity"
        },
        "answer": "C"
    },
    {
        "question": "Off-balance sheet transactions are required to be disclosed",
        "options": {
            "A": "in the management discussion and analysis.",
            "B": "in the auditor's report.",
            "C": "in the Securities and Exchange Commission's commentary.",
            "D": "in the statement of stockholders' equity."
        },
        "answer": "A"
    },
    {
        "question": "Details of acquisitions, spin-offs, leases, taxes, and risk management activities are given",
        "options": {
            "A": "in the management discussion and analysis.",
            "B": "in the Securities and Exchange Commission's commentary.",
            "C": "in the auditor's report.",
            "D": "in the notes to the financial statements."
        },
        "answer": "D"
    },
    {
        "question": "The Sarbanes-Oxley Act (SOX) was passed by Congress in 2002, in response to",
        "options": {
            "A": "financial scandals, including WorldCom and Enron.",
            "B": "financial scandals, including Bernie Madoff and AIG.",
            "C": "financial scandals, including General Motors and Chrysler.",
            "D": "the Troubled Asset Relief Program (TARP)."
        },
        "answer": "A"
    },
    {
        "question": "The largest stock market in the world is",
        "options": {
            "A": "the London Stock Exchange.",
            "B": "NASDAQ.",
            "C": "the American Stock Exchange.",
            "D": "the New York Stock Exchange."
        },
        "answer": "D"
    },
    {
        "question": "An investment is said to be liquid if the investment",
        "options": {
            "A": "has large day to day fluctuations in price.",
            "B": "has a large bid-ask spread.",
            "C": "can easily be converted into cash.",
            "D": "is traded on a stock exchange."
        },
        "answer": "C"
    },
    {
        "question": "What type of company trades on an organized stock exchange?",
        "options": {
            "A": "A limited liability company",
            "B": "A private company",
            "C": "An 'S' corporation",
            "D": "A public company"
        },
        "answer": "D"
    },
    {
        "question": "Which of the following statements is false?",
        "options": {
            "A": "On Nasdaq, stocks can and do have multiple market makers who compete with each other. Each market maker must post bid and ask prices in the Nasdaq network where they can be viewed by all participants.",
            "B": "Bid prices exceed ask prices.",
            "C": "Because customers always buy at the ask and sell at the bid, the bid-ask spread is a transaction cost investors have to pay in order to trade.",
            "D": "On the floor of the NYSE, market makers (known on the NYSE as specialists) match buyers and sellers."
        },
        "answer": "B"
    },
    {
        "question": "If you buy shares of Coca-Cola on the primary market,",
        "options": {
            "A": "Coca-Cola receives the money because the company has issued new shares.",
            "B": "you buy the shares from another investor who decided to sell the shares.",
            "C": "you buy the shares from the New York Stock Exchange.",
            "D": "you buy the shares from the Federal Reserve."
        },
        "answer": "A"
    },
    {
        "question": "If you buy shares of Coca-Cola on the secondary market,",
        "options": {
            "A": "Coca-Cola receives the money because the company has issued new shares.",
            "B": "you buy the shares from another investor who decided to sell the shares.",
            "C": "you buy the shares from the New York Stock Exchange.",
            "D": "you buy the shares from the Federal Reserve."
        },
        "answer": "B"
    },
    {
        "question": "Which of the following statements regarding the income statement is incorrect?",
        "options": {
            "A": "The income statement shows the earnings and expenses at a given point in time.",
            "B": "The income statement shows the flow of earnings and expenses generated by the firm between two dates.",
            "C": "The last or 'bottom' line of the income statement shows the firm's net income.",
            "D": "The first line of an income statement lists the revenues from the sales of products or services."
        },
        "answer": "A"
    },
    {
        "question": "Gross profit is calculated as:",
        "options": {
            "A": "Total sales - cost of sales - selling, general and administrative expenses - depreciation and amortization",
            "B": "Total sales - cost of sales - selling, general and administrative expenses",
            "C": "Total sales - cost of sales",
            "D": "None of the above"
        },
        "answer": "C"
    },
    {
        "question": "Which of the following is not an operating expense?",
        "options": {
            "A": "Interest expense",
            "B": "Depreciation and amortization",
            "C": "Selling, general and administrative expenses",
            "D": "Research and development"
        },
        "answer": "A"
    },
    {
        "question": "The firm's revenues and expenses over a period of time are reported on the firm's",
        "options": {
            "A": "income statement or statement of financial performance.",
            "B": "income statement or statement of financial position.",
            "C": "balance sheet or statement of financial performance.",
            "D": "balance sheet or statement of financial position."
        },
        "answer": "A"
    },
    {
        "question": "The statement of financial performance is also known as the",
        "options": {
            "A": "balance sheet.",
            "B": "income statement.",
            "C": "statement of cash flows.",
            "D": "statement of stockholder's equity."
        },
        "answer": "B"
    },
    {
        "question": "U.S. public companies are required to file their annual financial statements with the U.S. Securities and Exchange Commission on which form?",
        "options": {
            "A": "10-A",
            "B": "10-K",
            "C": "10-Q",
            "D": "10-SEC"
        },
        "answer": "B"
    },
    {
        "question": "Which of the following is not a financial statement that every public company is required to produce?",
        "options": {
            "A": "Income Statement",
            "B": "Statement of Sources and Uses of Cash",
            "C": "Balance Sheet",
            "D": "Statement of Stockholders' Equity"
        },
        "answer": "B"
    },
    {
        "question": "The third party who checks annual financial statements to ensure that they are prepared according to GAAP and verifies that the information reported is reliable is the",
        "options": {
            "A": "NYSE Enforcement Board.",
            "B": "Accounting Standards Board.",
            "C": "Securities and Exchange Commission (SEC).",
            "D": "auditor."
        },
        "answer": "D"
    },
    {
        "question": "Which of the following balance sheet equations is incorrect?",
        "options": {
            "A": "Assets - Liabilities = Shareholders' Equity",
            "B": "Assets = Liabilities + Shareholders' Equity",
            "C": "Assets - Current Liabilities = Long Term Liabilities",
            "D": "Assets - Current Liabilities = Long Term Liabilities + Shareholders' Equity"
        },
        "answer": "C"
    },
    {
        "question": "Cash is a",
        "options": {
            "A": "Long-term Asset.",
            "B": "Current Asset.",
            "C": "Current Liability.",
            "D": "Long-term Liability."
        },
        "answer": "B"
    },
    {
        "question": "Accounts payable is a",
        "options": {
            "A": "Long-term Liability.",
            "B": "Current Asset.",
            "C": "Long-term Asset.",
            "D": "Current Liability."
        },
        "answer": "D"
    },
    {
        "question": "A 30 year mortgage loan is a",
        "options": {
            "A": "Long-term Liability.",
            "B": "Current Liability.",
            "C": "Current Asset.",
            "D": "Long-term Asset."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following statements regarding the balance sheet is incorrect?",
        "options": {
            "A": "The balance sheet provides a snapshots of the firm's financial position at a given point in time.",
            "B": "The balance sheet lists the firm's assets and liabilities.",
            "C": "The balance sheet reports stockholders' equity on the right-hand side.",
            "D": "The balance sheet reports liabilities on the left-hand side."
        },
        "answer": "D"
    },
    {
        "question": "Dustin's Donuts experienced a decrease in the value of the trademark of a company it acquired two years ago. This reduction in value results in",
        "options": {
            "A": "an impairment charge.",
            "B": "depreciation expense.",
            "C": "an operating expense.",
            "D": "goodwill."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following is an example of an intangible asset?",
        "options": {
            "A": "Brand names and trademarks",
            "B": "Patents",
            "C": "Customer relationships",
            "D": "All of the above are intangible assets."
        },
        "answer": "D"
    },
    {
        "question": "On the balance sheet, short-term debt appears",
        "options": {
            "A": "in the Stockholders' Equity section.",
            "B": "in the Operating Expenses section.",
            "C": "in the Current Assets section.",
            "D": "in the Current Liabilities section."
        },
        "answer": "D"
    },
    {
        "question": "On the balance sheet, current maturities of long-term debt appear",
        "options": {
            "A": "in the Stockholders' Equity section.",
            "B": "in the Operating Expenses section.",
            "C": "in the Current Assets section.",
            "D": "in the Current Liabilities section."
        },
        "answer": "D"
    },
    {
        "question": "The firm's assets and liabilities at a given point in time are reported on the firm's",
        "options": {
            "A": "income statement or statement of financial performance.",
            "B": "income statement or statement of financial position.",
            "C": "balance sheet or statement of financial performance.",
            "D": "balance sheet or statement of financial position."
        },
        "answer": "D"
    },
    {
        "question": "The statement of financial position is also known as the",
        "options": {
            "A": "balance sheet.",
            "B": "income statement.",
            "C": "statement of cash flows.",
            "D": "statement of stockholder's equity."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following is not a reason why cash flow may not equal net income?",
        "options": {
            "A": "Amortization is added in when calculating net income.",
            "B": "Changes in inventory will change cash flows but not income.",
            "C": "Capital expenditures are not recorded on the income statement.",
            "D": "Depreciation is deducted when calculating net income."
        },
        "answer": "A"
    },
    {
        "question": "Which of the following adjustments to net income  is not correct if you are trying to calculate cash flow from operating activities?",
        "options": {
            "A": "Add increases in accounts payable",
            "B": "Add back depreciation",
            "C": "Add increases in accounts receivable",
            "D": "Deduct increases in inventory"
        },
        "answer": "C"
    },
    {
        "question": "Which of the following adjustments is not correct if you are trying to calculate cash flow from financing activities?",
        "options": {
            "A": "Add dividends paid",
            "B": "Add any increase in long term borrowing",
            "C": "Add any increase in short-term borrowing",
            "D": "Add proceeds from the sale of stock"
        },
        "answer": "A"
    },
    {
        "question": "In addition to the balance sheet, income statement, and the statement of cash flows, a firm's complete financial statements will include all of the following except:",
        "options": {
            "A": "Management discussion and Analysis",
            "B": "Notes to the financial statements",
            "C": "Securities and Exchange Commission's (SEC) commentary",
            "D": "Statement of stockholders' equity"
        },
        "answer": "C"
    },
    {
        "question": "Off-balance sheet transactions are required to be disclosed",
        "options": {
            "A": "in the management discussion and analysis.",
            "B": "in the auditor's report.",
            "C": "in the Securities and Exchange Commission's commentary.",
            "D": "in the statement of stockholders' equity."
        },
        "answer": "A"
    },
    {
        "question": "Details of acquisitions, spin-offs, leases, taxes, and risk management activities are given",
        "options": {
            "A": "in the management discussion and analysis.",
            "B": "in the Securities and Exchange Commission's commentary.",
            "C": "in the auditor's report.",
            "D": "in the notes to the financial statements."
        },
        "answer": "D"
    },
    {
        "question": "The Sarbanes-Oxley Act (SOX) was passed by Congress in 2002, in response to",
        "options": {
            "A": "financial scandals, including WorldCom and Enron.",
            "B": "financial scandals, including Bernie Madoff and AIG.",
            "C": "financial scandals, including General Motors and Chrysler.",
            "D": "the Troubled Asset Relief Program (TARP)."
        },
        "answer": "A"
    }
]

print("Initial questions structure:")
for idx, question in enumerate(questions):
    print(f"Question {idx + 1}: {question}")
    print(f" - Type of options: {type(question['options'])}")

# Duplicate questions to reach a total of 40
while len(questions) < 40:
    questions.extend(questions[:40 - len(questions)])

# Debugging: Print the structure of all duplicated questions to identify inconsistencies
print("Duplicated questions structure:")
for idx, question in enumerate(questions):
    print(f"Question {idx + 1}: {question}")
    print(f" - Type of options: {type(question['options'])}")

# Generate 5 different exams
exams = []
for i in range(5):
    random.shuffle(questions)
    selected_questions = questions[:40]
    answers = [q['answer'] for q in selected_questions]
    exam_pdf = generate_exam(selected_questions, answers)
    exams.append(exam_pdf)

# Save exams to PDF
save_directory = '/Users/rengvin/Downloads'
for i, exam in enumerate(exams, 1):
    file_path = f'{save_directory}/Finance_Exam_{i}.pdf'
    exam.output(file_path)
    print(f"Exam {i} saved as {file_path}")

    # Debugging print statements
    print(f"Selected Questions for Exam {i}:")
    for idx, question in enumerate(selected_questions):
        print(f"Question {idx + 1}: {question['question']}")
        print(f" - Options: {question['options']}")
        print(f" - Correct Answer: {question['answer']}")
