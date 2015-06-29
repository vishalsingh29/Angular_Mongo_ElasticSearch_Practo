angular.module('DoctorApp', ['ngRoute','DoctorControllers', 'DoctorServices'])
  .config(['$routeProvider', function($routeProvider){
  	console.log("hello")
    $routeProvider
    .when('/', {
        templateUrl: 'addDoctor.html', 
        controller:  "DoctorController"
      })
      .when('/bookslist', {
        templateUrl: 'static/addDoctor.html', 
        controller:  "DoctorController"
      })
  }]);