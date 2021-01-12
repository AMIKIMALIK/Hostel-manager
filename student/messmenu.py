from firebase import firebase

firebase = firebase.FirebaseApplication(
    "https://hostel-manager-7f13c.firebaseio.com/", None)

default_data = {
    "monday": {
        "breakfast": "Bread (4 P) + Butter/Jam + Banana (2 P)",
        "lunch": "Rice + Chapati + Dal + Salad + Chiken / Mushroom",
        "snacks": "Tea + Biscuits",
        "dinner": "Rice + Roti + Dal + Salad + Sabji"
    },
    "tuesday": {
        "breakfast": "Apple (1P 100g approx) + Banana (2P) + Chana (100g)",
        "lunch": "Rice + Chapati + Dal + Salad + Bhujia + Sabji",
        "snacks": "Tea + Mixture",
        "dinner": "Rice + Roti + Salad + Rajama"
    },
    "wednesday": {
        "breakfast": "Kachauri + Sabji",
        "lunch": "Rice + Chapati + Dal + Salad + Paneer",
        "snacks": "Tea + Kurkure",
        "dinner": "Rice +Roti + Chutni + Dal + Seasonal Veg"
    },
    "thrusday": {
        "breakfast": "Poha + Jalebi (2P)",
        "lunch": "Veg. Pulaw + Chapati + Salad + Tadka + Raita",
        "snacks": "Tea + Biscuits",
        "dinner": "Rice + Roti + Dal + Salad + Kofta + Sweet"
    },
    "friday": {
        "breakfast": "Bread (4 P) + Butter/Jam + Banana (2 P)",
        "lunch": "Rice + Chapati + Dal + Salad + Egg/Paneer",
        "snacks": "Tea + Mixture",
        "dinner": "Rice + Roti + Dal + Salad + Sabji + Kheer"
    },
    "saturday": {
        "breakfast": "Idly (4P) + Sambhar",
        "lunch": "Rice + Chapati + Dal + Salad + Mix Veg",
        "snacks": "Tea + Kurkure",
        "dinner": "Aloo Praatha + Chutni / Sauce"
    },
    "sunday": {
        "breakfast": "Chhola Bhatura",
        "lunch": "Veg. Pulaw / Jeera Rice + Aloo Dum + Salad",
        "snacks": "Tea + Bread Pakora",
        "dinner": "Roti + Sabji + Sweet"
    }

}

trans_data = {
    "busno": "104A",
    "time": "08:50AM",
    "from": "Beta2",
    "via": "IIMT, Jagat",
    "to": "GL Bajaj College"
}


def addmenu(mess, data):
    result = firebase.post(f"/hostel-manager-7f13c/{mess}", data)
    print(result)


def updatemenu():
    firebase.put(
        "/hostel-manager-7f13c/Customer/-MPZmGdhTIpnApyfUYUo", "Name", "Sumit Malik")


def retirivemenu():
    mess = "messmenu"
    table = '-MPbf16p99opnNtGkTrf'
    day = "monday"
    time = "breakfast"
    result = firebase.get(
        f"/hostel-manager-7f13c/{mess}/{table}/{day}/{time}", "")
    return result


def get_transport(id, first):
    result = firebase.get(f"/hostel-manager-7f13c/transport/{id}/{first}", "")
    return result


def add_tranport(data):
    res = firebase.post("/hostel-manager-7f13c/transport", data)
    # print(res)


def del_tranport():
    pass

# add_tranport(trans_data)
# get_transport()
