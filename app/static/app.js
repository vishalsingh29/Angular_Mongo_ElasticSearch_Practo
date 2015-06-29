var DoctorApp = angular.module('DoctorApp', ['ngRoute', 'DoctorControllers'])
  .config(['$routeProvider', '$locationProvider',  function($routeProvider, $locationProvider){
  	console.log("hello")
    $routeProvider
    .when('/', {
        templateUrl: 'static/index.html', 
        controller:  'DoctorController'
      })
      .when('/add_doctor', {
        templateUrl: 'static/addDoctor.html', 
        controller:  "DoctorController"
      })
      .when('/add_clinic', {
        templateUrl: 'static/EditClinicId.html', 
        controller:  "EditClinicController"
      })
      .when('/addClinic',{
      	templateUrl: 'static/AddClinic.html', 
        controller:  "DoctorController"
      })
      .when('/addSpecialization',{
      	templateUrl: 'static/AddSpecialization.html', 
        controller:  "DoctorController"
      })
      .when('/all_doctors',{
      	templateUrl:'static/Doctors.html',
      	controller:  "DoctorController"
      })
      .when('/AllClinic',{
      	templateUrl:'static/AllClinic.html',
      	controller:  "DoctorController"
      })
      .when('/AllSpecialization',{
      	templateUrl:'static/AllSpecialization.html',
      	controller:  "DoctorController"
      })
      .when('/edit_doctor',{
	    templateUrl: "static/EditDoctorId.html",
	    controller: "EditDoctorController"
  	})
      .when('/editDoctor',{
	    templateUrl: "static/EditDoctor.html",
	    controller: "DoctorController"
  	})
      .when('/EditClinic',{
	    templateUrl: "static/EditClinic.html",
	    controller: "DoctorController"
  	})
      .when('/EditSpecialization',{
	    templateUrl: "static/EditSpecialization.html",
	    controller: "DoctorController"
  	})

      .when('/edit_clinic',{
	    templateUrl: "static/EditClinicId.html",
	    controller: "EditClinicController"
  	})
      .when('/search',{
	    templateUrl: "static/Search.html",
	    controller: "SearchController"
  	})
      .when('/SearchName',{
	    templateUrl: "static/Doctors.html",
	    controller: "SearchController"
  	})

  }]);