$(function () {
	$.get({
		url: 'https://raw.githubusercontent.com/mateuv/cineclub/master/pelis.json',
		success: function (data) {
			console.log(data);
		},
		error: function (xhr) {
			console.log(xhr);
		}
	});
});
