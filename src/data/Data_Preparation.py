import Import_Packages

def Merge_Data(startNum, endNum, type_file, outputPath):
    startNum = 3
    endNum = 7
    type_file = 'enrolments'
    outputPath = '../data/processed/' + 'Merged' + str(startNum) + '-' + str(endNum) + '_' + type_file + '.csv'
    data_t = []
    for i in range(startNum,endNum+1):
        timesName = '-' + str(i) + '_'
        fileName = '../data/raw/Engagement of Cyber Serurity/dataset201819/cyber-security' + timesName + type_file + '.csv'
        data = pd.read_csv(fileName)
        data_t.append(data)

    
    mergedData = pd.concat(data_t)
    print('New merged data : ' + mergedData.shape)
    mergedData.info()
    mergedData.to_csv(outputPath)

    return mergedData

def Get_Loc():
    data = pd.read_csv('../data/processed/' +'Detected_Country' + '_157' + '.csv')
    lat = []
    lon = []
    count = 0
    for i in data['Country']:
        geolocator = Nominatim(user_agent="nnccll")
        location = geolocator.geocode(str(i))
        lat.append(str(location.latitude))
        lon.append(str(location.longitude))
        sleep(60)
    
    locations = []
    for i in range(len(lat)):
        locations.append((lat[i],lon[i]))
    lcts = pd.DataFrame(locations)
    lcts.to_csv('../data/external/Country-locations.csv')

def all_loc():
    merged_enrolment = pd.read_csv('../data/processed/Merged3-7_enrolments.csv' )
    locs = pd.read_csv('../data/external/Country-locations.csv')
    country_locs = pd.read_csv('../data/processed/Detected_Country_157.csv')
    country_locs = np.array(country_locs)
    country_locs = country_locs.tolist()
    tmp = []
    for i in country_locs:
        tmp.append(str(i[0]))
    
    locs = np.array(locs)
    locs = locs.tolist()
    locations = []
    for i in range(len(locs)):
        del locs[i][0]

    for i in merged_enrolment['detected_country']:
        if i not in tmp:
            pass
        else:
            locations.append(locs[tmp.index(i)])

    return locations

def country():

    return ud_country

def clean_AllCountry():

    return cleaned_country