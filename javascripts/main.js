function Movie(data) {
	var self = this;

	self.title          = ko.observable(data.title);
	self.original_title = ko.observable(data.original_title);
	self.director       = ko.observable(data.director);
	self.year           = ko.observable(data.year);
	self.country        = ko.observable(data.country);
	self.date           = ko.observable(data.date);
	self.fqn            = ko.observable(data.fqn);

	self.image = ko.pureComputed(function () {
		return 'https://raw.githubusercontent.com/mateuv/cineclub/master/proyecciones/'+
			self.date()+'_'+self.title()+
			'/poster.jpg';
	});
}

function MainViewModel() {
	var self = this;

	self.placeholder = ko.observable('Aguanta la vara...');
	self.items       = ko.observableArray([]);
	self.filter      = ko.observable('');
	self.shownItems  = ko.pureComputed(function () {
		return self.items().filter(function (item, index) {
			if (self.filter()) {
				return item.fqn().match(self.filter().toLowerCase());
			} else {
				return index < 10;
			}
		});
	});

	self.loadItems = function (items) {
		self.items(items.map(function (item) {
			return new Movie(item);
		}));
		self.placeholder('Escribe algo...');
	};

	self.load = function (done) {
		$.ajax({
			url: 'https://raw.githubusercontent.com/mateuv/cineclub/master/pelis.jsonp',
			jsonp: 'loadMovieData',
			dataType: 'jsonp',
			crossDomain: true,
			success: done,
			error: done
		});
	};
}

$(function () {
	window.mvm = new MainViewModel();

	mvm.load(function () {
		ko.applyBindings(mvm);
	});

});
