var app = angular.module('Main', ['ngRoute']);

app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider) {
 $routeProvider.
      when('/content/first', {
        templateUrl: 'first.html', 
        controller: 'first'
      }).
      when('/content/second', {
        templateUrl: 'second.html',
        controller: 'second'
      }); 
}]); 
 
app.controller('first', function($scope) {
  $scope.list = [1,2,3,4,5];
});

app.controller('second', function($scope) {
  $scope.list = [1,2,3];
});