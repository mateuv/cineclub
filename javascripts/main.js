function MainViewModel() {
	var self = this;

	self.items  = ko.observableArray([]);
	self.filter = ko.observable('');
	self.shownItems = ko.pureComputed(function () {
		return self.items().filter(function (item, index) {
			if (self.filter()) {
				return item.fqn.match(self.filter().toLowerCase());
			} else {
				return index < 10;
			}
		});
	});

	self.load = function (done) {
		$.ajax({
			url: '/pelis.jsonp',
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
