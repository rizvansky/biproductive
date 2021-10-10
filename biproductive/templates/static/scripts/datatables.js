let table_data = JSON.parse(JSON.parse(document.getElementById('habit_table_data').textContent))

let columns = []
for (let column in table_data[0]) {
    columns.push({data: column})
}
// columns.reverse()
// console.log("now reversed")
$('#habit_table').DataTable({
    data: table_data,
    columns: columns,
    responsive: true

});