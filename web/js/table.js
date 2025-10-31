let test_list = ["+",32,125,0,125,0,125]

console.log(test_list.length)

let doc = document;
let tbody = doc.getElementById("tbody");

let tr = doc.createElement('tr');
tr.class = "table-row-with-btn";

function createRow(list) {

    let tr = doc.createElement('tr');
    tr.class = "table-row-with-btn";

    list.forEach(item => {
        let td = doc.createElement('td');
        if (item == "+") {
            let span = doc.createElement('span');
            span.setAttribute("class","add-btn");
            span.setAttribute("data-bs-toggle","modal");
            span.setAttribute("data-bs-target","#paramsModal");
            span.innerText = "+";
            td.appendChild(span);
        }
        else {
            td.innerText = item;
        }
        tr.appendChild(td);
    });
    tbody.appendChild(tr);
}

createRow(test_list);