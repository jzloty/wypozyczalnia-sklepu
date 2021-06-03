const searchField = document.querySelector('#searchField');
const appTable = document.querySelector(".app-table");
const tbody = document.querySelector(".table-body");
const tableOutput = document.querySelector(".table-output");
tableOutput.style.display = "none";

searchField.addEventListener('keyup',(e)=>{
	const searchValue = e.target.value;

	if(searchValue.trim().length > 0){
		console.log('searchValue', searchValue)
		tbody.innerHTML = "";
		fetch("/szukajGry", {
			body: JSON.stringify({ szukanyText: searchValue }),
			method: "POST",
		})
		.then((res) => res.json())
		.then((data) => {
			console.log("data", data);

			appTable.style.display = "none";
			tableOutput.style.display = "block";

			if(data.length === 0){
				tableOutput.innerHTML = "Brak wyników";
			} else {
				data.forEach((item) => {
					var kolor = null;
					if(item.Data_orientacyjny_zwrot != null){
						 kolor = "table-danger";
					} else {
						kolor = "";
					}

					var data = null;
					if(item.Data_orientacyjny_zwrot != null){
						data = item.Data_orientacyjny_zwrot;
					} else {
						data = "";
					}
					tbody.innerHTML +=`
					<tr class=`+kolor+`>
						<td>${item.Tytul}</td>
						<td>${data}</td>
					</tr>`;
				});
			}
		});
	} else {
		appTable.style.display = "block";
		tableOutput.style.display = "none";
	}
});
