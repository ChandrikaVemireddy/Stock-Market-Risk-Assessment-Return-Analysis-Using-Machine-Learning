import requests

COMPANIES = {
    'SBIN': 'State Bank of India',
    'BHARTIARTL': 'Bharti Airtel Ltd.',
    'M&M': 'Mahindra & Mahindra Ltd.',
    'SUNPHARMA': 'Sun Pharmaceutical Industries Ltd.',
    'ITC': 'ITC Ltd.',
    'LT': 'Larsen & Toubro Ltd.',
    'NTPC': 'NTPC Ltd.',
    'TATASTEEL': 'Tata Steel Ltd.',
    'MARUTI': 'Maruti Suzuki India Ltd.',
    'HINDALCO': 'Hindalco Industries Ltd.'
}

START_DATE = '01-01-2019'
END_DATE = '31-12-2025'
BENCHMARK = 'NIFTY 50'

def create_session():
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json',
        'Referer': 'https://www.nseindia.com/'
    })
    return session

def main():
    session = create_session()
    session.get('https://www.nseindia.com/')
    print('NSE session initialized.')
    print('Companies:', len(COMPANIES))
    print('Period:', START_DATE, 'to', END_DATE)
    print('Benchmark:', BENCHMARK)

if __name__ == '__main__':
    main()
