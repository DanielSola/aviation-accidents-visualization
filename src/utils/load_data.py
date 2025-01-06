import pandas as pd

def normalize_make_model(make, model):
    # Normalize make
    upper_make = str(make).strip().upper()

    if upper_make == 'CESSNA': make = 'Cessna'
    if upper_make == 'PIPER': make = 'Piper'
    if upper_make == 'BOEING': make = 'Boeing'
    if upper_make == 'BEECH': make = 'Beech'
    if upper_make == 'BELL': make = 'Bell'
    if upper_make == 'MOONEY': make = 'Mooney'
    if upper_make == 'AIRBUS': make = 'Airbus'
    if upper_make == 'AIR TRACTOR': make = 'Air Tractor'
    if upper_make == 'HUGHES': make = 'Hughes'


    if 'A75N1' in model: model = 'A75N1'

    if upper_make == 'SCHWEIZER': make = 'Grumman'
    if 'ROBINSON' in upper_make: make = 'Robinson Helicopters'
    if 'CIRRUS' in upper_make: make = 'Cirrus Aircraft'


    if make == 'Robinson Helicopters' and '22' in model: model = 'R22'
    if make == 'Robinson Helicopters' and '44' in model: model = 'R44'

    if upper_make == 'HUGHES' and '369' in model: model = '369'
    if upper_make == 'CESSNA' and '17' in model: model = '172'
    if upper_make == 'CESSNA' and '15' in model: model = '152'
    if upper_make == 'CESSNA' and '18' in model: model = '182'
    if upper_make == 'CESSNA' and '210' in model: model = '210'
    if upper_make == 'CESSNA' and '402' in model: model = '402'
    if upper_make == 'CESSNA' and '208' in model: model = '208'
    if upper_make == 'CESSNA' and '340' in model: model = '340'
    if upper_make == 'CESSNA' and '310' in model: model = '310' 
    if upper_make == 'CESSNA' and '310' in model: model = '310'
    if upper_make == 'CESSNA' and '305' in model: model = '305'

    if upper_make == 'CESSNA' and '412' in model: model = '421'

    if upper_make == 'MOONEY' and 'M20' in model: model = 'M20'

    if upper_make == 'PIPER' and 'PA-28' in model: model = 'PA-28'
    if upper_make == 'PIPER' and 'PA 28' in model: model = 'PA-28'
    if upper_make == 'PIPER' and 'PA28' in model: model = 'PA-28'

    if upper_make == 'PIPER' and 'PA-18' in model: model = 'PA-18'
    if upper_make == 'PIPER' and 'PA 18' in model: model = 'PA-18'
    if upper_make == 'PIPER' and 'PA18' in model: model = 'PA-18'

    if upper_make == 'PIPER' and 'PA-38' in model: model = 'PA-38'
    if upper_make == 'PIPER' and 'PA 38' in model: model = 'PA-38'
    if upper_make == 'PIPER' and 'PA38' in model: model = 'PA-38'

    if upper_make == 'PIPER' and 'PA-32' in model: model = 'PA-32'
    if upper_make == 'PIPER' and 'PA 32' in model: model = 'PA-32'
    if upper_make == 'PIPER' and 'PA32' in model: model = 'PA-32'

    if upper_make == 'PIPER' and 'PA-24' in model: model = 'PA-24'
    if upper_make == 'PIPER' and 'PA 24' in model: model = 'PA-24'
    if upper_make == 'PIPER' and 'PA24' in model: model = 'PA-24'

    if upper_make == 'PIPER' and 'PA-34' in model: model = 'PA-34'
    if upper_make == 'PIPER' and 'PA 34' in model: model = 'PA-34'
    if upper_make == 'PIPER' and 'PA34' in model: model = 'PA-34'

    if upper_make == 'PIPER' and 'PA-24' in model: model = 'PA-24'
    if upper_make == 'PIPER' and 'PA 24' in model: model = 'PA-24'
    if upper_make == 'PIPER' and 'PA24' in model: model = 'PA-24'

    if upper_make == 'PIPER' and 'PA-23' in model: model = 'PA-23'
    if upper_make == 'PIPER' and 'PA 23' in model: model = 'PA-23'
    if upper_make == 'PIPER' and 'PA23' in model: model = 'PA-23'

    if upper_make == 'PIPER' and 'PA-22' in model: model = 'PA-22'
    if upper_make == 'PIPER' and 'PA 22' in model: model = 'PA-22'
    if upper_make == 'PIPER' and 'PA22' in model: model = 'PA-22'

    if upper_make == 'PIPER' and 'PA-31' in model: model = 'PA-31'
    if upper_make == 'PIPER' and 'PA 31' in model: model = 'PA-31'
    if upper_make == 'PIPER' and 'PA31' in model: model = 'PA-31'

    if upper_make == 'PIPER' and 'PA-25' in model: model = 'PA-25'
    if upper_make == 'PIPER' and 'PA 25' in model: model = 'PA-25'
    if upper_make == 'PIPER' and 'PA25' in model: model = 'PA-25'

    if upper_make == 'PIPER' and 'PA-12' in model: model = 'PA-12'
    if upper_make == 'PIPER' and 'PA 12' in model: model = 'PA-12'
    if upper_make == 'PIPER' and 'PA12' in model: model = 'PA-12'

    if upper_make == 'PIPER' and 'PA-44' in model: model = 'PA-44'
    if upper_make == 'PIPER' and 'PA 44' in model: model = 'PA-44'
    if upper_make == 'PIPER' and 'PA44' in model: model = 'PA-44'

    if upper_make == 'PIPER' and 'PA-30' in model: model = 'PA-30'
    if upper_make == 'PIPER' and 'PA 30' in model: model = 'PA-30'
    if upper_make == 'PIPER' and 'PA30' in model: model = 'PA-30'

    if upper_make == 'PIPER' and 'PA-60' in model: model = 'PA-60'
    if upper_make == 'PIPER' and 'PA 60' in model: model = 'PA-60'
    if upper_make == 'PIPER' and 'PA60' in model: model = 'PA-60'

    if upper_make == 'PIPER' and 'PA-46' in model: model = 'PA-46'
    if upper_make == 'PIPER' and 'PA 46' in model: model = 'PA-46'
    if upper_make == 'PIPER' and 'PA46' in model: model = 'PA-46'

    if upper_make == 'PIPER' and 'J3C' in model: model = 'J3C'


    if upper_make == 'BOEING' and '737' in model: model = '737'
    if upper_make == 'BOEING' and '747' in model: model = '747'
    if upper_make == 'BOEING' and '757' in model: model = '757'
    if upper_make == 'BOEING' and '777' in model: model = '777'
    if upper_make == 'BOEING' and '727' in model: model = '727'
    if upper_make == 'BOEING' and '787' in model: model = '787'
    if upper_make == 'BOEING' and '717' in model: model = '717'

    if make == 'Cirrus Aircraft' and '20' in model: model = 'SR22'
    if make == 'Cirrus Aircraft' and '22' in model: model = 'SR22'

    if 'AT-802' in model: model = 'AT-802'
    if 'AT802' in model: model = 'AT-802'

    if make == 'Grumman' and '164' in model: model = 'G-164'
    if upper_make == 'SCHWEIZER' and '164' in model: model = 'G-164'


    if upper_make == 'BELL' and '206' in model: model = '206'

    return make, model


def load_data():
    data = pd.read_csv('./data/AviationData.csv', encoding='ISO-8859-1', low_memory=False)
    
    # Convert columns to numeric, coercing errors
    data['Latitude'] = pd.to_numeric(data['Latitude'], errors='coerce')
    data['Longitude'] = pd.to_numeric(data['Longitude'], errors='coerce')
    data['Total.Fatal.Injuries'] = pd.to_numeric(data['Total.Fatal.Injuries'], errors='coerce').fillna(0)
    data['Total.Serious.Injuries'] = pd.to_numeric(data['Total.Serious.Injuries'], errors='coerce').fillna(0)
    data['Total.Minor.Injuries'] = pd.to_numeric(data['Total.Minor.Injuries'], errors='coerce').fillna(0)

    # Replace the values
    data["FAR.Description"] = data["FAR.Description"].replace('121', "Part 121: Air Carrier")
    data["FAR.Description"] = data["FAR.Description"].replace('091', "Part 91: General Aviation")
    data["FAR.Description"] = data["FAR.Description"].replace('137', "Part 137: Agricultural")
    data["FAR.Description"] = data["FAR.Description"].replace('129', "Part 129: Foreign Air Carriers")
    data["FAR.Description"] = data["FAR.Description"].replace('Part 129: Foreign', "Part 129: Foreign Air Carriers")
    data["FAR.Description"] = data["FAR.Description"].replace('125', "Part 125: 20+ Pax,6000+ lbs")
    data["FAR.Description"] = data["FAR.Description"].replace('135', "Part 135: Air Taxi & Commuter")
    data["FAR.Description"] = data["FAR.Description"].replace('Part 91F: Special Flt Ops.', "Part 91: General Aviation")
    data["FAR.Description"] = data["FAR.Description"].replace('091K', "Part 91: General Aviation")
    data["FAR.Description"] = data["FAR.Description"].replace('NUSN', "Non-U.S., Non-Commercial")
    data["FAR.Description"] = data["FAR.Description"].replace('NUSC', "Non-U.S., Commercial")
    data["FAR.Description"] = data["FAR.Description"].replace('133', "Part 133: Rotorcraft Ext. Load")
    data["FAR.Description"] = data["FAR.Description"].replace('UNK', "Unknown")
    data["FAR.Description"] = data["FAR.Description"].replace('PUBU', "Public Use")
    data["FAR.Description"] = data["FAR.Description"].replace('ARMF', "Armed Forces")
    data["FAR.Description"] = data["FAR.Description"].replace('Part 91 Subpart K: Fractional', "Part 91: General Aviation")
    data["FAR.Description"] = data["FAR.Description"].replace('107', "Part 107: Small Unmanned Aircraft Systems")
    data["FAR.Description"] = data["FAR.Description"].replace('103', "Part 103: Ultralight Vehicles")
    data["FAR.Description"] = data["FAR.Description"].replace('Public Use', "Public Aircraft")
    data["FAR.Description"] = data["FAR.Description"].replace('437', "Part 435: Experimental Permits")


    data.loc[(data["FAR.Description"] == "Non-U.S., Commercial"), "Purpose.of.flight"] = "Commercial"  
    data.loc[(data["FAR.Description"] == "Part 121: Air Carrier"), "Purpose.of.flight"] = "Commercial"  
    data.loc[(data["FAR.Description"] == "Part 129: Foreign Air Carriers"), "Purpose.of.flight"] = "Commercial"  
    data.loc[
        (data["Make"].str.upper().isin(['BOEING', 'AIRBUS', 'EMBRAER', 'DOUGLAS'])) & 
        (~data["Model"].str.contains("A75N1", na=False)), 
        "Purpose.of.flight"
    ] = "Commercial"

    data["Purpose.of.flight"] = data["Purpose.of.flight"].replace("Aerial Application", "Crop Dusting")
    data["Purpose.of.flight"] = data["Purpose.of.flight"].replace("Executive/corporate", "Business")
    data["Purpose.of.flight"] = data["Purpose.of.flight"].replace("Other Work Use", "Business")
    data["Purpose.of.flight"] = data["Purpose.of.flight"].replace("Air Race show", "Air Race/show")
    data["Purpose.of.flight"] = data["Purpose.of.flight"].replace("External Load", "Helicopter Training")
    data["Purpose.of.flight"] = data["Purpose.of.flight"].replace("Ferry", "Positioning")
    data["Purpose.of.flight"] = data["Purpose.of.flight"].replace("Ferry", "Positioning")
    data["Purpose.of.flight"] = data["Purpose.of.flight"].replace("Public Aircraft - Local", "Public Aircraft")
    data["Purpose.of.flight"] = data["Purpose.of.flight"].replace("Public Aircraft - State", "Public Aircraft")
    data["Purpose.of.flight"] = data["Purpose.of.flight"].replace("Public Aircraft - Federal", "Public Aircraft")

    data = data.dropna(subset=["Model"])

    data[["Make", "Model"]] = data.apply(
        lambda row: normalize_make_model(row["Make"], row["Model"]), axis=1, result_type="expand"
    )

    return data
    
