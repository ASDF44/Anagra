filename = "C:/Users/Saurabh/SDD/crop_by_state/state_wise_crop_distribution.txt"
file = open(filename, "r")
data_string = ''

for line in file:
   data_string = data_string + line
#print(data_string)

for char in data_string:
    if char in ",'":
       data_string = data_string.replace(char,'')
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
seasons = ['Kharif', 'Rabi']
process= ['Sowing','Harvesting']


data_list = data_string.split()
print(data_list)
