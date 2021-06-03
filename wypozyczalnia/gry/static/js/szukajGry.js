const searchField = document.querySelector('#searchField');

searchField.addEventListener('keyup',(e)=>{
	const searchValue = e.target.value;

	if(searchValue.trim().length > 0){
		console.log('searchValue', searchValue)

		fetch("/szukajGry", {
			body: JSON.stringify({ szukanyText: searchValue }),
			method: "POST",
		})
		.then((res) => res.json())
		.then((data) => {
			console.log("data", data);
		});
	}
});
