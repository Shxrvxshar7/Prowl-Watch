let menuicn = document.querySelector(".menuicn"); 
let nav = document.querySelector(".navcontainer"); 

menuicn.addEventListener("click", () => { 
	nav.classList.toggle("navclose"); 
})

let labelIcn = document.querySelectorAll(".label-tag");
console.log(labelIcn)

labelIcn.forEach(function (item) {
	item.addEventListener("click", function() {
		const loc = item.textContent.split(',');
		window.location.href = 'https://maps.google.com' + "/?q=" + loc[0] + ',' + loc[1];
	})
});

let viewLL = document.querySelector(".last-location-view");
viewLL.addEventListener("click", function () {
	const loc = labelIcn[0].textContent.split(',');
	window.location.href = 'https://maps.google.com' + "/?q=" + loc[0] + ',' + loc[1];
});
