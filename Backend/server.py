from flask import Flask
from flask import request
from flask_cors import CORS
import csv
import json

app = Flask(__name__)
CORS(app)

@app.route('/view-data', methods=['POST'])
def view_data():
    
    grade = request.json["grade"]
    section = request.json["section"]

    if grade == "9":
        csv_file1 = open('grade_9_records.csv', 'r')
        csv_reader = csv.DictReader(csv_file1)

        data = []
        for row in csv_reader:
            if row['section'] == section:
                data.append(row)
            elif section == "ALL":
                data.append(row)

        csv_file1.close()
        return json.dumps({"students": data})
    
    if grade == "10":
        csv_file1 = open('grade_10_records.csv', 'r')
        csv_reader = csv.DictReader(csv_file1)

        data = []
        for row in csv_reader:
            if row['section'] == section:
                data.append(row)
            elif section == "ALL":
                data.append(row)

        csv_file1.close()
        return json.dumps({"students": data})

    if grade == "11":
        csv_file1 = open('grade_11_records.csv', 'r')
        csv_reader = csv.DictReader(csv_file1)

        data = []
        for row in csv_reader:
            if row['section'] == section:
                data.append(row)
            elif section == "ALL":
                data.append(row)

        csv_file1.close()
        return json.dumps({"students": data})

    if grade == "12":
        csv_file1 = open('grade_12_records.csv', 'r')
        csv_reader = csv.DictReader(csv_file1)

        data = []
        for row in csv_reader:
            if row['section'] == section:
                data.append(row)
            elif section == "ALL":
                data.append(row)

        csv_file1.close()
        return json.dumps({"students": data})


@app.route('/student-details', methods=['POST'])
def studentDetails():
    id = request.json["roll_id"]
    get_data = []
    with open('grade_9_records.csv', 'r') as csv_file2:
        csv_reader = csv.DictReader(csv_file2)
        for row in csv_reader:
            if row["roll_id"] == id:
                get_data.append(row)
                break
    

    with open('grade_10_records.csv', 'r') as csv_file2:
        csv_reader = csv.DictReader(csv_file2)
        for row in csv_reader:
            if row["roll_id"] == id:
                get_data.append(row)
                break

    
    with open('grade_11_records.csv', 'r') as csv_file2:
        csv_reader = csv.DictReader(csv_file2)
        for row in csv_reader:
            if row["roll_id"] == id:
                get_data.append(row)
                break

    
    with open('grade_12_records.csv', 'r') as csv_file2:
        csv_reader = csv.DictReader(csv_file2)
        for row in csv_reader:
            if row["roll_id"] == id:
                get_data.append(row)
                break


    return json.dumps({"student": get_data})
    

@app.route('/new-entry', methods=['POST'])
def new_entry():

    name = request.json["name"]
    gen = request.json["gen"]
    dob = request.json["dob"]
    roll_id = request.json["roll_id"]
    grade = request.json["grade"]
    section = request.json["section"]
    phy = request.json["phy"]
    chem = request.json["chem"]
    ma = request.json["ma"]
    comp = request.json["comp"]
    eng = request.json["eng"]


    total = int(phy) + int(chem) + int(ma) + int(comp) + int(eng)
    max = 500
    percent = round(total / max * 100, 1)

    if int(phy) >= 34 and int(chem) >= 34 and int(ma) >= 34 and int(comp) >= 34 and int(eng) >= 34:
        status = "Pass"
    else:
        status = "Fail"

    post_data = [{
        "roll_id":roll_id, 
        "name":name, 
        "gen": gen, 
        "dob": dob, 
        "grade":grade, 
        "section":section, 
        "phy":phy, 
        "chem":chem, 
        "ma":ma, 
        "comp":comp, 
        "eng":eng, 
        "total":total, 
        "max":max,
        "percent":percent, 
        "status":status
    }]

    headers = [ "roll_id", "name", "gen", "dob", "grade", "section", "phy", "chem", "ma", "comp", "eng", "total", "max", "percent", "status" ]

    flag = False
    if grade == "9":
        with open('grade_9_records.csv', 'r') as csv_file2:
            csv_reader = csv.DictReader(csv_file2)
            for row in csv_reader:
                if row["roll_id"] == roll_id:
                    flag = True

        if flag == False:
            csv_file2 = open('grade_9_records.csv', 'a')
            csv_writer = csv.DictWriter(csv_file2, fieldnames = headers)

            csv_writer.writerows(post_data)

            csv_file2.close()

            return json.dumps({"message": "Added successfully"})
        else:
            return json.dumps({"message": "Student already exists"})

    elif grade == "10":
        with open('grade_10_records.csv', 'r') as csv_file2:
            csv_reader = csv.DictReader(csv_file2)
            for row in csv_reader:
                if row["roll_id"] == roll_id:
                    flag = True

        if flag == False: 
            csv_file2 = open('grade_10_records.csv', 'a')
            csv_writer = csv.DictWriter(csv_file2, fieldnames = headers)

            csv_writer.writerows(post_data)

            csv_file2.close()

            return json.dumps({"message": "Added successfully"})
        else:
            return json.dumps({"message": "Student already exists"})

    elif grade == "11":
        with open('grade_11_records.csv', 'r') as csv_file2:
            csv_reader = csv.DictReader(csv_file2)
            for row in csv_reader:
                if row["roll_id"] == roll_id:
                    flag = True

        if flag == False: 
            csv_file2 = open('grade_11_records.csv', 'a')
            csv_writer = csv.DictWriter(csv_file2, fieldnames = headers)

            csv_writer.writerows(post_data)

            csv_file2.close()

            return json.dumps({"message": "Added successfully"})
        else:
            return json.dumps({"message": "Student already exists"})


    elif grade == "12":
        with open('grade_12_records.csv', 'r') as csv_file2:
            csv_reader = csv.DictReader(csv_file2)
            for row in csv_reader:
                if row["roll_id"] == roll_id:
                    flag = True

        if flag == False: 
            csv_file2 = open('grade_12_records.csv', 'a')
            csv_writer = csv.DictWriter(csv_file2, fieldnames = headers)

            csv_writer.writerows(post_data)

            csv_file2.close()

            return json.dumps({"message": "Added successfully"})
        else:
            return json.dumps({"message": "Student already exists"})


@app.route('/student-details-edit', methods=['PATCH'])
def editStudentDetails():

    name = request.json["name"]
    roll_id = request.json["roll_id"]
    gen = request.json["gen"]
    dob = request.json["dob"]
    grade = request.json["grade"]
    section = request.json["section"]
    phy = request.json["phy"]
    chem = request.json["chem"]
    ma = request.json["ma"]
    comp = request.json["comp"]
    eng = request.json["eng"]

    total = int(phy) + int(chem) + int(ma) + int(comp) + int(eng)
    max = 500
    percent = round(total / max * 100, 1)

    if int(phy) >= 34 and int(chem) >= 34 and int(ma) >= 34 and int(comp) >= 34 and int(eng) >= 34:
        status = "Pass"
    else:
        status = "Fail"

    if grade == "9":
        with open('grade_9_records.csv', 'r') as csv_file3:
            csv_reader = csv.DictReader(csv_file3)
            records = []
            for row in csv_reader:
                records.append(row)

        for i in range(len(records)):
            if records[i]["roll_id"] == roll_id:
                records[i]["name"] = name
                records[i]["gen"] = gen
                records[i]["dob"] = dob
                records[i]["grade"] = grade
                records[i]["section"] = section
                records[i]["phy"] = phy
                records[i]["chem"] = chem
                records[i]["ma"] = ma
                records[i]["comp"] = comp
                records[i]["eng"] = eng
                records[i]["total"] = total
                records[i]["max"] = max
                records[i]["percent"] = percent
                records[i]["status"] = status
                break
        
        with open('grade_9_records.csv', 'w') as csv_file3:
            headers = records[0].keys()
            csv_writer = csv.DictWriter(csv_file3, fieldnames = headers)

            csv_writer.writeheader()

            for row in records:
                csv_writer.writerow(row)

        return "Updated Successfully"
    

    elif grade == "10":
        with open('grade_10_records.csv', 'r') as csv_file3:
            csv_reader = csv.DictReader(csv_file3)
            records = []
            for row in csv_reader:
                records.append(row)

        for i in range(len(records)):
            if records[i]["roll_id"] == roll_id:
                records[i]["name"] = name
                records[i]["gen"] = gen
                records[i]["dob"] = dob
                records[i]["grade"] = grade
                records[i]["section"] = section
                records[i]["phy"] = phy
                records[i]["chem"] = chem
                records[i]["ma"] = ma
                records[i]["comp"] = comp
                records[i]["eng"] = eng
                records[i]["total"] = total
                records[i]["max"] = max
                records[i]["percent"] = percent
                records[i]["status"] = status
                break
        
        with open('grade_10_records.csv', 'w') as csv_file3:
            headers = records[0].keys()
            csv_writer = csv.DictWriter(csv_file3, fieldnames = headers)

            csv_writer.writeheader()

            for row in records:
                csv_writer.writerow(row)

        return "Updated Successfully"


    elif grade == "11":
        with open('grade_11_records.csv', 'r') as csv_file3:
            csv_reader = csv.DictReader(csv_file3)
            records = []
            for row in csv_reader:
                records.append(row)

        for i in range(len(records)):
            if records[i]["roll_id"] == roll_id:
                records[i]["name"] = name
                records[i]["gen"] = gen
                records[i]["dob"] = dob
                records[i]["grade"] = grade
                records[i]["section"] = section
                records[i]["phy"] = phy
                records[i]["chem"] = chem
                records[i]["ma"] = ma
                records[i]["comp"] = comp
                records[i]["eng"] = eng
                records[i]["total"] = total
                records[i]["max"] = max
                records[i]["percent"] = percent
                records[i]["status"] = status
                break
        
        with open('grade_11_records.csv', 'w') as csv_file3:
            headers = records[0].keys()
            csv_writer = csv.DictWriter(csv_file3, fieldnames = headers)

            csv_writer.writeheader()

            for row in records:
                csv_writer.writerow(row)

        return "Updated Successfully"


    if grade == "12":
        with open('grade_12_records.csv', 'r') as csv_file3:
            csv_reader = csv.DictReader(csv_file3)
            records = []
            for row in csv_reader:
                records.append(row)

        for i in range(len(records)):
            if records[i]["roll_id"] == roll_id:
                records[i]["name"] = name
                records[i]["gen"] = gen
                records[i]["dob"] = dob
                records[i]["grade"] = grade
                records[i]["section"] = section
                records[i]["phy"] = phy
                records[i]["chem"] = chem
                records[i]["ma"] = ma
                records[i]["comp"] = comp
                records[i]["eng"] = eng
                records[i]["total"] = total
                records[i]["max"] = max
                records[i]["percent"] = percent
                records[i]["status"] = status
                break
        
        with open('grade_12_records.csv', 'w') as csv_file3:
            headers = records[0].keys()
            csv_writer = csv.DictWriter(csv_file3, fieldnames = headers)

            csv_writer.writeheader()

            for row in records:
                csv_writer.writerow(row)

        return "Updated Successfully"


@app.route('/student-delete', methods=['DELETE'])
def deleteStudent():
    roll_id = request.json["roll_id"]
    if roll_id[0] == "9":
        with open('grade_9_records.csv', 'r') as csv_file3:
            csv_reader = csv.DictReader(csv_file3)
            records = []
            for row in csv_reader:
                if row["roll_id"] != roll_id:
                    records.append(row)

        with open('grade_9_records.csv', 'w') as csv_file3:
            headers = records[0].keys()
            csv_writer = csv.DictWriter(csv_file3, fieldnames = headers)

            csv_writer.writeheader()

            for row in records:
                csv_writer.writerow(row)

        return "Deleted Successfully"


    elif roll_id[0]+roll_id[1] == "10":
        with open('grade_10_records.csv', 'r') as csv_file3:
            csv_reader = csv.DictReader(csv_file3)
            records = []
            for row in csv_reader:
                if row["roll_id"] != roll_id:
                    records.append(row)

        with open('grade_10_records.csv', 'w') as csv_file3:
            headers = records[0].keys()
            csv_writer = csv.DictWriter(csv_file3, fieldnames = headers)

            csv_writer.writeheader()

            for row in records:
                csv_writer.writerow(row)

        return "Deleted Successfully"


    elif roll_id[0]+roll_id[1] == "11":
        with open('grade_11_records.csv', 'r') as csv_file3:
            csv_reader = csv.DictReader(csv_file3)
            records = []
            for row in csv_reader:
                if row["roll_id"] != roll_id:
                    records.append(row)

        with open('grade_11_records.csv', 'w') as csv_file3:
            headers = records[0].keys()
            csv_writer = csv.DictWriter(csv_file3, fieldnames = headers)

            csv_writer.writeheader()

            for row in records:
                csv_writer.writerow(row)

        return "Deleted Successfully"
    

    elif roll_id[0]+roll_id[1] == "12":
        with open('grade_12_records.csv', 'r') as csv_file3:
            csv_reader = csv.DictReader(csv_file3)
            records = []
            for row in csv_reader:
                if row["roll_id"] != roll_id:
                    records.append(row)

        with open('grade_12_records.csv', 'w') as csv_file3:
            headers = records[0].keys()
            csv_writer = csv.DictWriter(csv_file3, fieldnames = headers)

            csv_writer.writeheader()

            for row in records:
                csv_writer.writerow(row)

        return "Deleted Successfully"