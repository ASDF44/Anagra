import pandas as pd

data = {
'ANDHRA PRADESH': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Blackgram/Urd', 'Kharif', 'June', '(Beg)', 'July', '(Beg)', 'Sowing', 'Kharif', 'June', '(Mid)', 'July', '(Mid)', 'Sowing', 'Kharif', 'June', '(Beg)', 'December', '(End)', 'Harvesting', 'Kharif', 'September', '(Beg)', 'September', '(End)', 'Harvesting', 'Rabi', 'November', '(Mid)', 'January', '(End)', 'Sowing', 'Rabi', 'October', '(Beg)', 'January', '(Mid)', 'Sowing', 'Rabi', 'February', '(Mid)', 'April', '(End)', 'Harvesting', 'Chick', 'Pea', 'Kharif', 'January', '(Beg)', 'September', '(Mid)', 'Sowing', 'Rabi', 'October', '(Beg)', 'February', '(Mid)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Rabi', 'October', '(Beg)', 'February', '(Mid)', 'Sowing', 'Rabi', 'October', '(Beg)', 'February', '(Mid)', 'Sowing', 'Rabi', 'August', '(Beg)', 'February', '(Mid)', 'Harvesting', 'Rabi', 'August', '(Beg)', 'January', '(Mid)', 'Harvesting', 'Rabi', 'August', '(Beg)', 'December', '(Beg)', 'Harvesting', 'Rabi', 'August', '(Beg)', 'October', '(Beg)', 'Harvesting', 'Rabi', 'November', '(Beg)', 'February', '(Beg)', 'Harvesting', 'Rabi', 'November', '(Beg)', 'February', '(Beg)', 'Harvesting', 'Rabi', 'November', '(Beg)', 'February', '(Beg)', 'Harvesting', 'Gram', 'Rabi', 'October', '(Beg)', 'December', '(Beg)', 'Sowing', 'Greengram', 'Kharif', 'July', '(Beg)', 'October', '(Beg)', 'Sowing', 'Kharif', 'June', '(Mid)', 'July', '(Mid)', 'Sowing', 'Kharif', 'October', '(Beg)', 'January', '(Beg)', 'Sowing', 'Kharif', 'August', '(Mid)', 'September', '(Beg)', 'Harvesting', 'Rabi', 'November', '(Mid)', 'December', '(End)', 'Sowing', 'Rabi', 'February', '(Beg)', 'April', '(Beg)', 'Sowing', 'Rabi', 'February', '(End)', 'March', '(Mid)', 'Harvesting', 'Summer', 'April', '(Beg)', 'April', '(Beg)', 'Sowing', 'Summer', 'April', '(Beg)', 'April', '(Beg)', 'Sowing', 'Horsegram', 'Early', 'Kharif', 'August', '(Beg)', 'January', '(Mid)', 'Sowing', 'Maize', 'Kharif', 'June', '(Beg)', 'August', '(Mid)', 'Sowing', 'Kharif', 'January', '(Beg)', 'January', '(Mid)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'January', '(Mid)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'January', '(Mid)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'January', '(Beg)', 'Harvesting', 'Rabi', 'November', '(End)', 'March', '(Beg)', 'Harvesting', 'Peas', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Kharif', 'March', '(Beg)', 'June', '(End)', 'Sowing', 'Pulses', 'Early', 'Kharif', 'August', '(Beg)', 'October', '(Beg)', 'Sowing', 'Kharif', 'August', '(Beg)', 'October', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'September', '(Beg)', 'Sowing', 'Rabi', 'October', '(Beg)', 'January', '(Mid)', 'Sowing', 'Rabi', 'August', '(Beg)', 'October', '(Beg)', 'Sowing', 'Redgram/Arhar', 'Kharif', 'August', '(Beg)', 'October', '(Beg)', 'Sowing', 'Kharif', 'June', '(Mid)', 'July', '(Mid)', 'Sowing', 'Kharif', 'January', '(Mid)', 'February', '(Mid)', 'Harvesting', 'Rabi', 'August', '(Beg)', 'October', '(Beg)', 'Sowing', 'Rabi', 'December', '(Beg)', 'February', '(Mid)', 'Sowing', 'Rice/Paddy', 'Early', 'Kharif', 'May', '(Beg)', 'August', '(Beg)', 'Sowing', 'Early', 'Kharif', 'May', '(Beg)', 'August', '(Beg)', 'Sowing', 'Kharif', 'August', '(Beg)', 'November', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'July', '(Beg)', 'Sowing', 'Kharif', 'July', '(Beg)', 'November', '(Mid)', 'Sowing', 'Kharif', 'June', '(Beg)', 'February', '(Mid)', 'Sowing', 'Kharif', 'January', '(Beg)', 'July', '(Mid)', 'Sowing', 'Kharif', 'January', '(Beg)', 'July', '(Mid)', 'Sowing', 'Kharif', 'October', '(Beg)', 'March', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'August', '(End)', 'Sowing', 'Kharif', 'June', '(Beg)', 'September', '(Beg)', 'Sowing', 'Kharif', 'July', '(Beg)', 'November', '(Mid)', 'Sowing', 'Kharif', 'September', '(Beg)', 'January', '(Beg)', 'Sowing', 'Kharif', 'March', '(Beg)', 'June', '(End)', 'Sowing', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Harvesting', 'Kharif', 'June', '(Beg)', 'October', '(Beg)', 'Harvesting', 'Kharif', 'October', '(End)', 'February', '(Beg)', 'Harvesting', 'Kharif', 'July', '(Beg)', 'November', '(Mid)', 'Harvesting', 'Kharif', 'June', '(Beg)', 'October', '(Beg)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'December', '(Beg)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'December', '(Beg)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Harvesting', 'Rabi', 'December', '(Beg)', 'April', '(Beg)', 'Sowing', 'Rabi', 'February', '(Beg)', 'May', '(Mid)', 'Sowing', 'Rabi', 'February', '(Beg)', 'July', '(Mid)', 'Sowing', 'Rabi', 'November', '(End)', 'February', '(Beg)', 'Sowing', 'Rabi', 'March', '(End)', 'May', '(Mid)', 'Harvesting', 'Wheat', 'Rabi', 'October', '(Beg)', 'January', '(Mid)', 'Sowing', ''],

'ARUNACHALPRADESH' : ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Maize', 'Kharif', 'June', '(Mid)', 'October', '(Mid)', 'Sowing', ''],

'ASSAM': [ '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Blackgram/Urd', 'Rabi', 'August','(Beg)', 'September', '(End)', 'Sowing', 'Rabi', 'October', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'November', '(Beg)', 'December', '(End)', 'Harvesting', 'Summer', 'February', '(Beg)', 'April', '(Beg)', 'Sowing', 'Summer', 'February', '(Beg)', 'April', '(Beg)', 'Sowing', 'Gram', 'Kharif', 'August', '(Beg)', 'November', '(Beg)', 'Sowing', 'Greengram', 'Rabi', 'August', '(Beg)', 'September', '(End)', 'Sowing', 'Rabi', 'November', '(Beg)', 'December', '(End)', 'Harvesting', 'Maize', 'Rabi', 'January', '(Beg)', 'May', '(Beg)', 'Sowing', 'Summer', 'January', '(Beg)', 'December', '(Beg)', 'Sowing', 'Masur/Lentil', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'March', '(Beg)', 'April', '(End)', 'Harvesting', 'Pulses', 'Early', 'Kharif', 'January', '(Beg)', 'June', '(Beg)', 'Sowing', 'Summer', 'March', '(Beg)', 'June', '(Beg)', 'Sowing', 'Rice/Paddy', 'Early', 'Kharif', 'January', '(Beg)', 'January', '(Beg)', 'Sowing', 'Kharif', 'June', '(Mid)', 'July', '(End)', 'Sowing', 'Kharif', 'October', '(Beg)', 'February', '(End)', 'Harvesting', 'Kharif', 'May', '(Beg)', 'July', '(Beg)', 'Harvesting', 'Summer', 'March', '(Beg)', 'June', '(Beg)', 'Sowing', 'Wheat', 'Rabi', 'January', '(Beg)', 'May', '(Beg)', 'Sowing', 'Rabi', 'November', '(Beg)', 'December', '(Mid)', 'Sowing', 'Rabi', 'March', '(Beg)', 'April', '(End)', 'Harvesting'],

'BIHAR': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Greengram', 'Kharif', 'April', '(Beg)', 'July', '(Beg)', 'Sowing', 'Masur/Lentil', 'Kharif', 'June', '(Mid)', 'July', '(Beg)', 'Sowing', 'Kharif', 'November', '(Beg)', 'December', '(End)', 'Harvesting', 'Rabi', 'October', '(Mid)', 'November', '(Mid)', 'Sowing', 'Rabi', 'March', '(Beg)', 'March', '(End)', 'Harvesting', 'Pulses', 'Rabi', 'January', '(Beg)', 'April', '(Beg)', 'Sowing', 'Rice/Paddy', 'Kharif', 'June', '(Mid)', 'July', '(Beg)', 'Sowing', 'Kharif', 'January', '(Mid)', 'July', '(Beg)', 'Sowing', 'Kharif', 'November', '(End)', 'December', '(End)', 'Harvesting', 'Wheat', 'Rabi', 'November', '(Mid)', 'December', '(End)', 'Sowing', 'Rabi', 'March', '(Mid)', 'April', '(End)', 'Harvesting', ''],

'CHHATTISGARH': [ '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Masur/Lentil', 'Kharif', 'August', '(Beg)', 'September', '(End)', 'Sowing', 'Kharif', 'November', '(Beg)', 'December', '(End)', 'Harvesting', 'Rabi', 'December', '(Beg)', 'January', '(End)', 'Sowing', 'Rabi', 'March', '(Beg)', 'May', '(End)', 'Harvesting', 'Redgram/Arhar', 'Rabi', 'December', '(Beg)', 'April', '(Beg)', 'Sowing', 'Rice/Paddy', 'Rabi', 'January', '(Beg)', 'May', '(Beg)', 'Sowing', 'Rabi', 'January', '(Beg)', 'May', '(Beg)', 'Sowing', 'Rabi', 'January', '(Beg)', 'January', '(Beg)', 'Sowing', 'Rabi', 'January', '(Beg)', 'January', '(Beg)', 'Sowing'],

'GUJARAT': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Gram', 'Kharif', 'October', '(Mid)', 'January', '(Beg)', 'Harvesting', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'February', '(Beg)', 'March', '(End)', 'Harvesting', 'Greengram', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Rabi', 'June', '(Beg)', 'August', '(Beg)', 'Sowing', 'Maize', 'Kharif', 'April', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'November', '(Mid)', 'March', '(Beg)', 'Sowing', 'Rabi', 'November', '(Mid)', 'March', '(Beg)', 'Sowing', 'Rabi', 'November', '(Beg)', 'March', '(Beg)', 'Sowing', 'Rabi', 'November', '(Beg)', 'March', '(Beg)', 'Sowing', 'Rabi', 'November', '(Beg)', 'March', '(Beg)', 'Sowing', 'Pulses', 'Rabi', 'March', '(Beg)', 'June', '(Beg)', 'Sowing', 'Rice/Paddy', 'Kharif', 'January', '(Beg)', 'November', '(Beg)', 'Sowing', 'Kharif', 'May', '(Mid)', 'July', '(Mid)', 'Sowing', 'Kharif', 'July', '(Beg)', 'December', '(Beg)', 'Harvesting', 'Kharif', 'October', '(Beg)', 'December', '(End)', 'Harvesting', 'Wheat', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'November', '(Beg)', 'April', '(Beg)', 'Sowing', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'November', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'October', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'October', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'December', '(Beg)', 'January', '(Beg)', 'Sowing', 'Rabi', 'November', '(Beg)', 'February', '(Mid)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Harvesting', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Harvesting', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Harvesting', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Harvesting', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Harvesting', 'Rabi', 'February', '(Beg)', 'March', '(End)', 'Harvesting'],

'HARYANA':['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Chick', 'Pea', 'Rabi', 'November', '(Beg)', 'April', '(Beg)', 'Sowing', 'Gram', 'Rabi', 'October', '(Beg)', 'October', '(Mid)', 'Sowing', 'Rabi', 'March', '(Mid)', 'March', '(End)', 'Harvesting', 'Peas', 'Rabi', 'November', '(Beg)', 'January', '(Beg)', 'Sowing', 'Pulses', 'Rabi', 'January', '(Beg)', 'December', '(End)', 'Harvesting', 'Rice/Paddy', 'Kharif', 'June', '(Beg)', 'July', '(Beg)', 'Sowing', 'Kharif', 'January', '(Beg)', 'December', '(Mid)', 'Sowing', 'Kharif', 'June', '(Beg)', 'July', '(Beg)', 'Sowing', 'Kharif', 'October', '(Mid)', 'November', '(End)', 'Harvesting', 'Wheat', 'Rabi', 'October', '(End)', 'December', '(Beg)', 'Sowing', 'Rabi', 'April', '(Mid)', 'April', '(End)', 'Harvesting', ''],

'HIMACHAL PRADESH': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Rice/Paddy', 'Kharif', 'May', '(Mid)', 'July', '(End)', 'Sowing', 'Kharif', 'September', '(Mid)', 'October', '(Mid)', 'Harvesting', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Wheat', 'Rabi', 'April', '(Mid)', 'June', '(End)', 'Harvesting', ''],

'JAMMU AND KASHMIR': ['Rice/Paddy', 'Kharif', 'May', '(Beg)', 'June', '(End)', 'Sowing', 'Kharif', 'October', '(Beg)', 'November', '(End)', 'Harvesting', 'Wheat', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'May', '(Beg)', 'May', '(End)', 'Harvesting', ''],

'JHARKHAND': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Horsegram', 'Kharif', 'June', '(Beg)', 'October', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'October', '(Beg)', 'Sowing', 'Rice/Paddy', 'Kharif', 'June', '(Beg)', 'October', '(Beg)', 'Sowing', ''],

'KARNATAKA': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Blackgram/Urd', 'Kharif', 'May', '(Beg)', 'August', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'July', '(End)', 'Sowing', 'Kharif', 'September', '(Beg)', 'October', '(End)', 'Harvesting', 'Rabi', 'November', '(Mid)', 'November', '(Mid)', 'Sowing', 'Rabi', 'October', '(Beg)', 'November', '(Beg)', 'Sowing', 'Rabi', 'December', '(Mid)', 'March', '(Beg)', 'Harvesting', 'Rabi', 'September', '(Beg)', 'October', '(End)', 'Harvesting', 'Rabi', 'December', '(Beg)', 'January', '(End)', 'Harvesting', 'Summer', 'February', '(Beg)', 'March', '(Beg)', 'Sowing', 'Chick', 'Pea', 'Rabi', 'August', '(Beg)', 'October', '(Beg)', 'Harvesting', 'Gram', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'January', '(Beg)', 'March', '(End)', 'Harvesting', 'Greengram', 'Early', 'Kharif', 'May', '(Beg)', 'July', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'July', '(End)', 'Sowing', 'Kharif', 'June', '(Beg)', 'July', '(Beg)', 'Sowing', 'Kharif', 'September', '(Beg)', 'October', '(End)', 'Harvesting', 'Rabi', 'September', '(Beg)', 'October', '(End)', 'Sowing', 'Rabi', 'December', '(Beg)', 'January', '(End)', 'Harvesting', 'Horsegram', 'Kharif', 'September', '(Mid)', 'January', '(Beg)', 'Sowing', 'Maize', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Rabi', 'December', '(Beg)', 'March', '(Beg)', 'Sowing', 'Summer', 'April', '(Beg)', 'August', '(Beg)', 'Sowing', 'Summer', 'April', '(Beg)', 'August', '(Beg)', 'Sowing', 'Summer', 'April', '(Beg)', 'August', '(Beg)', 'Sowing', 'Peas', 'Rabi', 'August', '(Beg)', 'December', '(Beg)', 'Sowing', 'Redgram/Arhar', 'Kharif', 'June', '(Beg)', 'July', '(End)', 'Sowing', 'Kharif', 'November', '(Beg)', 'February', '(End)', 'Harvesting', 'Rabi', 'January', '(Beg)', 'June', '(Beg)', 'Sowing', 'Rabi', 'January', '(Beg)', 'June', '(Beg)', 'Sowing', 'Rice/Paddy', 'Kharif', 'January', '(Beg)', 'January', '(Beg)', 'Sowing', 'Kharif', 'May', '(Beg)', 'July', '(End)', 'Sowing', 'Kharif', 'October', '(Beg)', 'December', '(End)', 'Harvesting', 'Kharif', 'July', '(Mid)', 'June', '(Mid)', 'Harvesting', 'Kharif', 'July', '(Mid)', 'June', '(Mid)', 'Harvesting', 'Rabi', 'August', '(Beg)', 'September', '(End)', 'Sowing', 'Rabi', 'January', '(Beg)', 'February', '(End)', 'Harvesting', 'Wheat', 'Rabi', 'October', '(Beg)', 'February', '(End)', 'Sowing', 'Rabi', 'October', '(Beg)', 'October', '(Beg)', 'Sowing', 'Rabi', 'October', '(Beg)', 'October', '(Beg)', 'Sowing', 'Rabi', 'July', '(Beg)', 'October', '(Beg)', 'Sowing', 'Rabi', 'January', '(Beg)', 'February', '(End)', 'Harvesting', ''],

'KERALA' : ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Blackgram/Urd', 'Kharif', 'March', '(Beg)', 'June', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'September', '(End)', 'Harvesting', 'Summer', 'September', '(Beg)', 'October', '(End)', 'Sowing', 'Summer', 'November', '(Beg)', 'December', '(End)', 'Harvesting', 'Greengram', 'Kharif', 'September', '(Beg)', 'November', '(End)', 'Sowing', 'Kharif', 'November', '(Beg)', 'November', '(End)', 'Harvesting', 'Summer', 'September', '(Beg)', 'October', '(End)', 'Sowing', 'Summer', 'November', '(Beg)', 'December', '(End)', 'Harvesting', 'Redgram/Arhar', 'Early', 'Kharif', 'May', '(Beg)', 'August', '(Beg)', 'Sowing', 'Early', 'Kharif', 'August', '(Beg)', 'October', '(End)', 'Harvesting', 'Kharif', 'August', '(Beg)', 'November', '(End)', 'Sowing', 'Kharif', 'October', '(Beg)', 'February', '(End)', 'Harvesting', 'Summer', 'February', '(Beg)', 'March', '(End)', 'Sowing', 'Summer', 'May', '(Beg)', 'May', '(End)', 'Harvesting', 'Rice/Paddy', 'Kharif', 'July', '(Beg)', 'June', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'December', '(End)', 'Sowing', 'Kharif', 'August', '(Beg)', 'November', '(End)', 'Sowing', 'Kharif', 'November', '(Beg)', 'January', '(End)', 'Harvesting', 'Rabi', 'October', '(Beg)', 'December', '(End)', 'Sowing', 'Rabi', 'March', '(Beg)', 'May', '(End)', 'Harvesting', ''],

'MADHYA PRADESH': [ '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Blackgram/Urd', 'Kharif', 'June', '(Mid)', 'August', '(Mid)', 'Sowing', 'Kharif', 'September', '(Mid)', 'November', '(End)', 'Harvesting', 'Kharif', 'June', '(Beg)', 'November', '(Beg)', 'Harvesting', 'Kharif', 'June', '(Beg)', 'December', '(Beg)', 'Harvesting', 'Rabi', 'October', '(Mid)', 'November', '(End)', 'Sowing', 'Rabi', 'February', '(Mid)', 'May', '(Mid)', 'Harvesting', 'Rabi', 'September', '(Beg)', 'June', '(Beg)', 'Harvesting', 'Chick', 'Pea', 'Rabi', 'October', '(Mid)', 'March', '(Beg)', 'Sowing', 'Rabi', 'January', '(Beg)', 'February', '(Beg)', 'Harvesting', 'Rabi', 'February', '(Beg)', 'March', '(Beg)', 'Harvesting', 'Gram', 'Rabi', 'October', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'September', '(Beg)', 'June', '(Beg)', 'Harvesting', 'Rabi', 'February', '(Beg)', 'April', '(Beg)', 'Harvesting', 'Greengram', 'Kharif', 'June', '(Mid)', 'August', '(Mid)', 'Sowing', 'Kharif', 'September', '(Mid)', 'December', '(Mid)', 'Harvesting', 'Kharif', 'June', '(Beg)', 'November', '(Beg)', 'Harvesting', 'Rabi', 'October', '(Mid)', 'December', '(Mid)', 'Sowing', 'Rabi', 'February', '(Beg)', 'May', '(Beg)', 'Harvesting', 'Summer', 'March', '(Beg)', 'June', '(Beg)', 'Sowing', 'Summer', 'April', '(Beg)', 'June', '(Beg)', 'Sowing', 'Maize', 'Kharif', 'January', '(Beg)', 'December', '(Beg)', 'Sowing', 'Summer', 'June', '(Beg)', 'July', '(Mid)', 'Sowing', 'Masur/Lentil', 'Rabi', 'September', '(Mid)', 'November', '(End)', 'Sowing', 'Rabi', 'February', '(Mid)', 'April', '(Beg)', 'Harvesting', 'Peas', 'Kharif', 'June', '(Beg)', 'November', '(Beg)', 'Harvesting', 'Rabi', 'October', '(Beg)', 'October', '(End)', 'Sowing', 'Redgram/Arhar', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Rabi', 'February', '(Beg)', 'April', '(Beg)', 'Sowing', 'Rice/Paddy', 'Kharif', 'January', '(Beg)', 'January', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'August', '(Beg)', 'Sowing', 'Kharif', 'January', '(Beg)', 'January', '(Beg)', 'Sowing', 'Kharif', 'June', '(Mid)', 'July', '(End)', 'Sowing', 'Kharif', 'September', '(End)', 'December', '(End)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'May', '(End)', 'Harvesting', 'Wheat', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Harvesting', 'Rabi', 'December', '(End)', 'January', '(Beg)', 'Sowing', 'Rabi', 'October', '(Mid)', 'December', '(End)', 'Sowing', 'Rabi', 'January', '(Beg)', 'October', '(Beg)', 'Harvesting', 'Rabi', 'October', '(Beg)', 'March', '(Mid)', 'Harvesting', 'Rabi', 'January', '(Beg)', 'April', '(Mid)', 'Harvesting', 'Rabi', 'March', '(Beg)', 'May', '(Beg)', 'Harvesting', 'Rabi', 'February', '(Beg)', 'March', '(Beg)', 'Harvesting', 'Rabi', 'February', '(Mid)', 'April', '(End)', 'Harvesting', 'Rabi', 'January', '(Beg)', 'December', '(End)', 'Harvesting', 'Summer', 'May', '(Beg)', 'May', '(Beg)', 'Harvesting', ''],

'MAHARASHTRA': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Blackgram/Urd', 'Kharif', 'July', '(Beg)', 'August', '(End)', 'Sowing', 'Kharif', 'October', '(Beg)', 'October', '(End)', 'Harvesting', 'Chick', 'Pea', 'Kharif', 'April', '(Beg)', 'March', '(Beg)', 'Harvesting', 'Rabi', 'December', '(Beg)', 'March', '(Mid)', 'Sowing', 'Rabi', 'April', '(Beg)', 'March', '(Beg)', 'Harvesting', 'Rabi', 'January', '(Beg)', 'December', '(End)', 'Harvesting', 'Rabi', 'April', '(Beg)', 'March', '(Beg)', 'Harvesting', 'Gram', 'Kharif', 'August', '(Beg)', 'January', '(Mid)', 'Sowing', 'Rabi', 'September', '(Beg)', 'February', '(Beg)', 'Sowing', 'Rabi', 'September', '(Beg)', 'March', '(Beg)', 'Sowing', 'Rabi', 'September', '(Beg)', 'October', '(End)', 'Sowing', 'Rabi', 'February', '(Beg)', 'March', '(End)', 'Harvesting', 'Greengram', 'Kharif', 'July', '(Beg)', 'July', '(End)', 'Sowing', 'Kharif', 'June', '(Beg)', 'October', '(Beg)', 'Sowing', 'Kharif', 'January', '(Beg)', 'January', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'October', '(Beg)', 'Sowing', 'Kharif', 'August', '(Beg)', 'September', '(End)', 'Harvesting', 'Rabi', 'April', '(Beg)', 'June', '(Beg)', 'Sowing', 'Rabi', 'December', '(Beg)', 'May', '(Beg)', 'Sowing', 'Maize', 'Kharif', 'June', '(Beg)', 'December', '(Beg)', 'Sowing', 'Kharif', 'November', '(Mid)', 'February', '(Mid)', 'Sowing', 'Kharif', 'January', '(Beg)', 'January', '(Beg)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'January', '(Beg)', 'Harvesting', 'Rabi', 'January', '(Beg)', 'December', '(End)', 'Harvesting', 'Summer', 'January', '(Beg)', 'December', '(End)', 'Harvesting', 'Redgram/Arhar', 'Kharif', 'June', '(Beg)', 'December', '(Beg)', 'Sowing', 'Kharif', 'July', '(Beg)', 'July', '(End)', 'Sowing', 'Kharif', 'December', '(Beg)', 'January', '(End)', 'Harvesting', 'Rice/Paddy', 'Kharif', 'July', '(Beg)', 'August', '(End)', 'Sowing', 'Kharif', 'May', '(Beg)', 'November', '(Mid)', 'Sowing', 'Kharif', 'October', '(Beg)', 'December', '(End)', 'Harvesting', 'Rabi', 'December', '(Beg)', 'January', '(Beg)', 'Harvesting', 'Summer', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Summer', 'May', '(Beg)', 'June', '(Beg)', 'Sowing', 'Summer', 'May', '(Beg)', 'June', '(Beg)', 'Harvesting', 'Summer', 'January', '(Beg)', 'December', '(End)', 'Harvesting', 'Wheat', 'Rabi', 'October', '(Beg)', 'December', '(End)', 'Sowing', 'Rabi', 'November', '(Beg)', 'March', '(Mid)', 'Sowing', 'Rabi', 'February', '(Beg)', 'March', '(End)', 'Harvesting', ''],

'ODISHA': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Blackgram/Urd', 'Kharif', 'April', '(Beg)', 'June', '(Beg)', 'Sowing', 'Kharif', 'April', '(Beg)', 'June', '(Beg)', 'Harvesting', 'Greengram', 'Rabi', 'October', '(Mid)', 'January', '(Beg)', 'Sowing', 'Pulses', 'Rabi', 'January', '(Beg)', 'April', '(Beg)', 'Harvesting', 'Rice/Paddy', 'Kharif', 'June', '(Beg)', 'January', '(End)', 'Sowing', 'Kharif', 'June', '(Beg)', 'August', '(Beg)', 'Sowing', 'Kharif', 'December', '(Beg)', 'January', '(Beg)', 'Harvesting', 'Rabi', 'December', '(Beg)', 'January', '(Beg)', 'Sowing', 'Rabi', 'December', '(Beg)', 'April', '(Beg)', 'Sowing', 'Rabi', 'December', '(Beg)', 'May', '(Beg)', 'Sowing', 'Rabi', 'September', '(Mid)', 'December', '(Mid)', 'Sowing', 'Rabi', 'September', '(Mid)', 'December', '(Mid)', 'Sowing', 'Rabi', 'December', '(Beg)', 'May', '(Beg)', 'Sowing', 'Rabi', 'May', '(Beg)', 'June', '(Beg)', 'Harvesting', 'Wheat', 'Rabi', 'October', '(Beg)', 'November', '(Beg)', 'Sowing', 'Rabi', 'March', '(Beg)', 'April', '(Beg)', 'Harvesting', ''],

'PUNJAB': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Greengram', 'Kharif', 'June', '(Beg)', 'July', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'July', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'July', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'July', '(Beg)', 'Sowing', 'Kharif', 'August', '(Beg)', 'October', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'July', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'July', '(Beg)', 'Sowing', 'Kharif', 'August', '(Beg)', 'October', '(Beg)', 'Harvesting', 'Kharif', 'August', '(Beg)', 'October', '(Beg)', 'Harvesting', 'Kharif', 'August', '(Beg)', 'October', '(Beg)', 'Harvesting', 'Masur/Lentil', 'Kharif', 'June', '(Beg)', 'July', '(End)', 'Sowing', 'Rabi', 'September', '(Beg)', 'October', '(End)', 'Harvesting', 'Peas', 'Early', 'Kharif', 'May', '(Beg)', 'July', '(Beg)', 'Harvesting', 'Rabi', 'September', '(Beg)', 'October', '(Beg)', 'Sowing', 'Rice/Paddy', 'Kharif', 'May', '(Beg)', 'July', '(End)', 'Sowing', 'Kharif', 'September', '(Beg)', 'October', '(End)', 'Harvesting', 'Rabi', 'January', '(Beg)', 'January', '(Beg)', 'Sowing', 'Wheat', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'April', '(Beg)', 'May', '(End)', 'Harvesting', ''],

'RAJASTHAN': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Blackgram/Urd', 'Kharif', 'July', '(Beg)', 'August', '(End)', 'Sowing', 'Kharif', 'October', '(Beg)', 'November', '(End)', 'Harvesting', 'Gram', 'Rabi', 'August', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'August', '(Beg)', 'December', '(Beg)', 'Sowing', 'Greengram', 'Kharif', 'July', '(Beg)', 'August', '(End)', 'Sowing', 'Kharif', 'October', '(Beg)', 'October', '(End)', 'Harvesting', 'Peas', 'Rabi', 'October', '(Beg)', 'November', '(Beg)', 'Sowing', 'Rabi', 'October', '(Beg)', 'November', '(Beg)', 'Sowing', 'Pulses', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Kharif', 'June', '(Beg)', 'October', '(Beg)', 'Sowing', 'Redgram/Arhar', 'Kharif', 'June', '(Mid)', 'March', '(Beg)', 'Sowing', 'Kharif', 'July', '(Beg)', 'July', '(End)', 'Sowing', 'Kharif', 'December', '(Beg)', 'January', '(End)', 'Harvesting', 'Rice/Paddy', 'Kharif', 'June', '(Beg)', 'July', '(End)', 'Sowing', 'Kharif', 'October', '(Beg)', 'November', '(End)', 'Harvesting', 'Wheat', 'Kharif', 'November', '(Beg)', 'May', '(Mid)', 'Sowing', 'Kharif', 'November', '(Beg)', 'May', '(Mid)', 'Sowing', 'Kharif', 'January', '(Beg)', 'April', '(Beg)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'April', '(Beg)', 'Harvesting', 'Kharif', 'July', '(Mid)', 'October', '(End)', 'Harvesting', 'Rabi', 'November', '(Beg)', 'March', '(Beg)', 'Sowing', 'Rabi', 'November', '(Beg)', 'December', '(End)', 'Sowing', 'Rabi', 'March', '(Beg)', 'May', '(End)', 'Harvesting', ''],

'TAMIL_NADU': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Blackgram/Urd', 'Kharif', 'August', '(Beg)', 'December', '(Beg)', 'Sowing', 'Kharif', 'October', '(Mid)', 'December', '(Mid)', 'Sowing', 'Greengram', 'Summer', 'November', '(End)', 'March', '(Beg)', 'Sowing', 'Horsegram', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Summer', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Summer', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Maize', 'Kharif', 'February', '(Beg)', 'January', '(Beg)', 'Sowing', 'Rabi', 'December', '(Beg)', 'January', '(Beg)', 'Sowing', 'Rabi', 'December', '(Beg)', 'January', '(Beg)', 'Sowing', 'Rice/Paddy', 'Early', 'Kharif', 'June', '(Beg)', 'June', '(Beg)', 'Harvesting', 'Early', 'Kharif', 'June', '(Beg)', 'June', '(Beg)', 'Harvesting', 'Kharif', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Summer', 'January', '(Beg)', 'April', '(Beg)', 'Sowing', ''],

'UTTAR PRADESH':  ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Blackgram/Urd', 'Rabi', 'April', '(Beg)', 'April', '(End)', 'Sowing', 'Rabi', 'June', '(Beg)', 'June', '(Mid)', 'Harvesting', 'Summer', 'April', '(Beg)', 'June', '(End)', 'Sowing', 'Chick', 'Pea', 'Kharif', 'October', '(Mid)', 'October', '(Mid)', 'Sowing', 'Gram', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'March', '(Beg)', 'April', '(End)', 'Harvesting', 'Rabi', 'April', '(Beg)', 'June', '(End)', 'Harvesting', 'Greengram', 'Kharif', 'September', '(Beg)', 'December', '(Beg)', 'Sowing', 'Kharif', 'October', '(Mid)', 'October', '(Mid)', 'Sowing', 'Rabi', 'April', '(Beg)', 'June', '(End)', 'Harvesting', 'Summer', 'April', '(Beg)', 'April', '(End)', 'Sowing', 'Summer', 'June', '(Beg)', 'June', '(End)', 'Harvesting', 'Maize', 'Kharif', 'June', '(Beg)', 'October', '(Beg)', 'Sowing', 'Masur/Lentil', 'Rabi', 'October', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'March', '(Beg)', 'March', '(End)', 'Harvesting', 'Peas', 'Rabi', 'April', '(Beg)', 'July', '(Beg)', 'Sowing', 'Rabi', 'April', '(Beg)', 'June', '(End)', 'Harvesting', 'Rabi', 'April', '(Beg)', 'June', '(End)', 'Harvesting', 'Redgram/Arhar', 'Kharif', 'October', '(Mid)', 'April', '(Beg)', 'Sowing', 'Kharif', 'January', '(Beg)', 'July', '(End)', 'Sowing', 'Kharif', 'January', '(Beg)', 'January', '(Mid)', 'Harvesting', 'Kharif', 'March', '(Beg)', 'April', '(Mid)', 'Harvesting', 'Rice/Paddy', 'Kharif', 'July', '(Beg)', 'October', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'August', '(End)', 'Sowing', 'Kharif', 'October', '(Beg)', 'December', '(Mid)', 'Harvesting', 'Kharif', 'October', '(Beg)', 'December', '(Mid)', 'Harvesting', 'Wheat', 'Rabi', 'October', '(Beg)', 'January', '(Mid)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'February', '(Beg)', 'August', '(Beg)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'October', '(Beg)', 'March', '(Beg)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(Beg)', 'Sowing', 'Rabi', 'April', '(Beg)', 'April', '(Mid)', 'Harvesting', ''],

'UTTARAKHAND': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Peas', 'Kharif', 'October', '(Beg)', 'October', '(Mid)', 'Sowing', ''],

'WEST BENGAL': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'Blackgram/Urd', 'Early', 'Kharif', 'March', '(Beg)', 'June', '(Beg)', 'Sowing', 'Early', 'Kharif', 'March', '(Beg)', 'March', '(Beg)', 'Sowing', 'Early', 'Kharif', 'March', '(Beg)', 'March', '(Beg)', 'Sowing', 'Gram', 'Rabi', 'November', '(Mid)', 'December', '(Beg)', 'Sowing', 'Rabi', 'March', '(Beg)', 'March', '(End)', 'Harvesting', 'Summer', 'March', '(Beg)', 'July', '(Beg)', 'Sowing', 'Greengram', 'Kharif', 'July', '(Beg)', 'August', '(End)', 'Sowing', 'Kharif', 'October', '(Beg)', 'November', '(End)', 'Harvesting', 'Summer', 'February', '(Beg)', 'March', '(End)', 'Sowing', 'Summer', 'April', '(Beg)', 'May', '(End)', 'Harvesting', 'Masur/Lentil', 'Rabi', 'February', '(Beg)', 'April', '(Beg)', 'Sowing', 'Rabi', 'February', '(Beg)', 'April', '(Beg)', 'Sowing', 'Rabi', 'November', '(Beg)', 'November', '(End)', 'Sowing', 'Rabi', 'February', '(Beg)', 'May', '(Beg)', 'Sowing', 'Rabi', 'February', '(Beg)', 'March', '(End)', 'Harvesting', 'Summer', 'June', '(Beg)', 'April', '(Beg)', 'Sowing', 'Pulses', 'Summer', 'May', '(Beg)', 'July', '(Beg)', 'Sowing', 'Summer', 'May', '(Beg)', 'July', '(Beg)', 'Sowing', 'Redgram/Arhar', 'Kharif', 'June', '(Beg)', 'June', '(End)', 'Sowing', 'Kharif', 'February', '(Beg)', 'March', '(End)', 'Harvesting', 'Rice/Paddy', 'Kharif', 'June', '(Beg)', 'September', '(Beg)', 'Sowing', 'Kharif', 'June', '(Beg)', 'August', '(End)', 'Sowing', 'Kharif', 'July', '(Beg)', 'August', '(Mid)', 'Sowing', 'Kharif', 'June', '(Beg)', 'August', '(Mid)', 'Sowing', 'Kharif', 'July', '(Beg)', 'August', '(Mid)', 'Sowing', 'Kharif', 'November', '(Beg)', 'January', '(End)', 'Harvesting', 'Rabi', 'January', '(Beg)', 'February', '(End)', 'Sowing', 'Rabi', 'April', '(Beg)', 'May', '(End)', 'Harvesting', 'Wheat', 'Rabi', 'November', '(Beg)', 'December', '(End)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Rabi', 'January', '(Beg)', 'December', '(End)', 'Sowing', 'Rabi', 'March', '(Beg)', 'April', '(End)', 'Harvesting', ''],
}

for key in data:
    n = data[key].count('')
    for i in range(n):
        data[key].remove('')

state_crop = pd.DataFrame(data)
print(state_crop)