let table_data = JSON.parse(JSON.parse(document.getElementById('habit_table_data').textContent))

let columns = []
console.log("columns", columns)
for (let column in table_data[0]) {
    columns.push({data: column})
}
console.log(columns)

$('#habit_table').DataTable({
    data: table_data,
    columns,

});