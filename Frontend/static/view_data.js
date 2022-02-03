var viewData = document.querySelector(".view-data");

function goToStudent(roll_id){
    console.log(roll_id);
    localStorage.setItem("student", JSON.stringify(roll_id));
    window.location.replace("./student_details.html");
}

async function collect_data(grade, section) {
    const args = {
        grade: grade,
        section: section,
    };
    await fetch("http://127.0.0.1:5000/view-data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(args),
    })
        .then((resp) => resp.json())
        .then((resp) => {
            console.log(resp);
            viewData.innerHTML = "";
            function sortByRoll(a, b) {
                if (a.roll_id < b.roll_id) {
                    return -1;
                }
                if (a.roll_id > b.roll_id) {
                    return 1;
                }
                return 0;
            }
            resp.students.sort(sortByRoll);
            var table = document.createElement("table");
            var row_1 = document.createElement("tr");
            
            table.setAttribute("class", "view-data-table");
            row_1.setAttribute("class", "view-data-row_1");
            const headers = ["#", "ID", "Name", "Grade", "Section", "Physics", "Chemistry", "Maths", "Computer", "English", "Total Marks", "Max Marks", "Percentage", "Status"];
            for (var i = 0; i < 14; i++) {
                var th = document.createElement("th");
                th.setAttribute("class", "view-data-th");
                th.innerHTML = headers[i];
                row_1.appendChild(th);
            }
            table.appendChild(row_1);
            var body = document.createElement("tbody");
            body.setAttribute("class", "view-data-body");
            resp.students.forEach((record, i) => {
                var tr = document.createElement("tr");
                tr.setAttribute("class", "view-data-tr");
                const cells = [i + 1, record.roll_id, record.name, record.grade, record.section, record.phy, record.chem, record.ma, record.comp, record.eng, record.total, record.max, record.percent, record.status]
                for (var j = 0; j < 14; j++) {
                    var td = document.createElement("td");
                    if(j == 0){
                        td.innerHTML = cells[j];
                        td.setAttribute("class", "view-data-first-column");
                    }
                    else if(j == 1){
                        var div = document.createElement("div");
                        div.innerHTML = cells[j];
                        div.addEventListener("click", function(){goToStudent(record.roll_id)});
                        div.setAttribute("class", "links-text");
                        td.setAttribute("class", "view-data-td");
                        td.append(div);
                    }
                    else if(j == 13){
                        td.innerHTML = cells[j];
                        if(td.innerHTML == "Pass"){
                            td.setAttribute("class", "view-data-pass");
                        }
                        else{
                            td.setAttribute("class", "view-data-fail");
                        }
                    }
                    else{
                        td.innerHTML = cells[j];
                        td.setAttribute("class", "view-data-td");
                    }
                    tr.appendChild(td);;
                }
                body.appendChild(tr);
            });
            table.appendChild(body);
            viewData.appendChild(table);
        })
        .catch((error) => console.log(error));
}

function get_data(e) {
    e.preventDefault();
    var grade = document.getElementById("grade").value;
    var section = document.getElementById("section").value;
    if (section === "default" || grade === "default") {
        alert("Please select both Section and Grade!");
    } else {
        console.log(grade + " " + section);
        collect_data(grade, section);
    }
}
