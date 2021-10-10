let table_data = JSON.parse(JSON.parse(document.getElementById('habit_table_data').textContent))

let columns = JSON.parse(JSON.parse(document.getElementById('datatables_js_cols').textContent))['cols']
let cols = []
for (let column in columns) {
    cols.push({data: columns[column]})
}

$('#habit_table').DataTable({
    data: table_data,
    columns: cols,
    responsive: true

});