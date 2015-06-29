angular.module('DoctorControllers',[])
  .controller('DoctorController', function($scope,$http,$location,$q,$rootScope){
  		$http.get('/doctor')
        .success(function(data, status, headers, config){
          $scope.doctors = data['results'];
          console.log($scope.doctors)
      });
    $scope.addDoctor = function(){
  	var req = {
      method: 'POST',
      url: 'http://localhost:5000/clinic',
      headers: {'Content-Type': 'application/json'},
      data: {first_name: $scope.first_name, last_name:$scope.last_name,area:$scope.area, city:$scope.city, experience_in_year:$scope.experience_in_year,experience_in_month:$scope.experience_in_month,phone_number:$scope.phone_number,email:$scope.email,specialization:$scope.specialization,education:$scope.education,description:$scope.description}
    };

   $http.post('/doctor', req['data'])
        .success(function(data, status, headers, config){
          console.log(data);
      });
        $location.path('/all_doctors');
  	}
	 $scope.editDoctor = function(doctor){
	    $rootScope.doctor = doctor;
	    $location.path('/editDoctor');
  	}
  	$scope.allClinic = function(user){
  		$rootScope.clinics = user.clinics;
  		$rootScope.id = user['_id']['$oid'];
  		console.log(user)
  		console.log($rootScope.clinics);
  		$location.path('/AllClinic');
  	}
  	$scope.allSpecialization = function(user){
  		$rootScope.specializations = user.specialization;
  		$rootScope.id = user['_id']['$oid'];
  		console.log(user)
  		console.log($rootScope.specializations);
  		$location.path('/AllSpecialization');
  	}

  	$scope.removeDoctor = function(doctor){
  		console.log(doctor['_id']['$oid']);
  		var q = 'http://127.0.0.1:5000/doctor/'+String(doctor['_id']['$oid']);
  		$http.delete(q)
        .success(function(data, status, headers, config){
      });
  		$location.path('/');
  	}
  	$scope.EditClinic = function(id,index, user){
  		$rootScope.id = id;
  		$rootScope.index = index;
  		$rootScope.clinic = user;
  		$location.path('/EditClinic');

  	}
  	$scope.EditSpecialization = function(id,index, user){
  		$rootScope.id = id;
  		$rootScope.index = index;
  		$rootScope.specialization = user;
  		$location.path('/EditSpecialization');

  	}
  	$scope.DeleteClinic = function(id, index){
  		var q = 'http://127.0.0.1:5000/delete_clinic/' + String(id)+"/"+String(index);
  		$http.delete(q)
        .success(function(data, status, headers, config){
      });
  		$location.path('/');
  	}
  	$scope.DeleteSpecialization = function(id, index){
  		var q = 'http://127.0.0.1:5000/delete_specialization/' + String(id)+"/"+String(index);
  		$http.delete(q)
        .success(function(data, status, headers, config){
      });
  		$location.path('/');
  	}
  	
  	$scope.editClinic = function(){
  		console.log($rootScope.id, $rootScope.index);
  		var req = {
      	headers: {'Content-Type': 'application/json'},
      	data: {name:$scope.clinic.name,city:$scope.clinic.city,area:$scope.clinic.area,complete_address:$scope.clinic.complete_address, fee:$scope.clinic.fee,timings:$scope.clinic.timings}
    	};
    	var q = 'http://127.0.0.1:5000/update_clinic/'+String($rootScope.id)+"/"+String($rootScope.index);
    	$http.post(q,req['data'])
        .success(function(data, status, headers, config){
      });
  		$location.path('/');
  	}
  	$scope.editSpecialization = function(){
  		console.log($rootScope.id, $rootScope.index);
  		var req = {
      	headers: {'Content-Type': 'application/json'},
      	data: {name:$scope.specialization}
    	};
    	var q = 'http://127.0.0.1:5000/update_specialization/'+String($rootScope.id)+"/"+String($rootScope.index);
    	$http.post(q,req['data'])
        .success(function(data, status, headers, config){
      });
  		$location.path('/');
  	}
  	$scope.addClinic = function(user){
  		$rootScope.id = user['_id']['$oid'];
  		console.log($rootScope.id);
  		$location.path('/addClinic');
  	}
  	$scope.addSpecialization = function(user){
  		$rootScope.user = user;
  		$location.path('/addSpecialization');
  	}
  	$scope.AddSpecialization = function(){
		console.log($scope.user['_id']['$oid']);
  		var q = 'http://127.0.0.1:5000/add_specialization/'+String($scope.user['_id']['$oid']);
  		console.log(q, $scope.specialization);
  		var req = {
	      method: 'POST',
	      url: 'http://localhost:5000/add_specialization',
	      headers: {'Content-Type': 'application/json'},
	      data: {specialization:$scope.specialization}
	    };
  		// doc = {first_name:$rootScope.first_name,last_name:$rootScope.last_name,phone_number:$rootScope.phone_number,city:$rootScope.city,area:$rootScope.area,experience_in_year:$rootScope.experience_in_year,education:$rootScope.education,email:$rootScope.email}
		// console.log("Hello",req['data']);
		$http.post(q, req['data'])
        .success(function(data, status, headers, config){
          // console.log(data);
      });
      $location.path('/');
  	}
  	$scope.AddClinic = function(user){
		console.log($scope.id);
  		var q = 'http://127.0.0.1:5000/add_clinic/'+String($scope.id);
  		console.log(q);
  		var req = {
	      method: 'POST',
	      url: 'http://localhost:5000/clinic',
	      headers: {'Content-Type': 'application/json'},
	      data: {name: $scope.name, city:$scope.city,area:$scope.area,complete_address:$scope.complete_address ,timings:$scope.timing,fee:$scope.fee}
	    };
  		// doc = {first_name:$rootScope.first_name,last_name:$rootScope.last_name,phone_number:$rootScope.phone_number,city:$rootScope.city,area:$rootScope.area,experience_in_year:$rootScope.experience_in_year,education:$rootScope.education,email:$rootScope.email}
		// console.log("Hello",req['data']);
		$http.post(q, req['data'])
        .success(function(data, status, headers, config){
          // console.log(data);
      });
      $location.path('/');
  	}
  	$scope.EditDoctor = function(){
  		console.log($scope.doctor['_id']['$oid']);
  		var q = 'http://127.0.0.1:5000/doctor/'+String($scope.doctor['_id']['$oid']);
  		console.log(q);
  		var req = {
	      method: 'POST',
	      url: 'http://localhost:5000/clinic',
	      headers: {'Content-Type': 'application/json'},
	      data: {first_name:$scope.doctor.first_name,last_name:$scope.doctor.last_name,phone_number:$scope.doctor.phone_number,city:$scope.doctor.city,area:$scope.doctor.area,experience_in_year:$scope.doctor.experience_in_year,education:$scope.doctor.education,email:$scope.doctor.email,description:$scope.doctor.description}
	    };
  		// doc = {first_name:$rootScope.first_name,last_name:$rootScope.last_name,phone_number:$rootScope.phone_number,city:$rootScope.city,area:$rootScope.area,experience_in_year:$rootScope.experience_in_year,education:$rootScope.education,email:$rootScope.email}
		// console.log("Hello",req['data']);
		$http.post(q, req['data'])
        .success(function(data, status, headers, config){
          // console.log(data);
      });
      $location.path('/');
  	}
  })
.controller('ClinicController', function($scope,$http,$location,$q){
	$scope.addClinic = function(){
  	var req = {
      method: 'POST',
      url: 'http://localhost:5000/clinic',
      headers: {'Content-Type': 'application/json'},
      data: {name: $scope.name, city:$scope.city,area:$scope.area,complete_address:$scope.complete_address}
    };
   $http.post('/clinic', req['data'])
        .success(function(data, status, headers, config){
          console.log(data);
      });
  	}
  	$http.get('/clinic')
        .success(function(data, status, headers, config){
          $scope.clinics = data['results'];
          console.log($scope.clinics)
      });
})
.controller('EditDoctorController', function($scope,$http,$location,$q,$rootScope){
	$scope.getDoctor = function(){
		$rootScope.id = $scope.Id;
		var q = 'http://127.0.0.1:5000/doctor/'+String($scope.Id);
		$http.get(q)
        .success(function(data, status, headers, config){
          $rootScope.doctor = data['results'];
          console.log($scope.doctor);
      });
      $location.path('/editDoctor');
  	}
  	$scope.EditDoctor = function(){
  		console.log($rootScope.doctor);
  		var q = 'http://127.0.0.1:5000/doctor/'+String($rootScope.id);
  		var req = {
	      method: 'POST',
	      url: 'http://localhost:5000/clinic',
	      headers: {'Content-Type': 'application/json'},
	      data: {first_name:$scope.doctor.first_name,last_name:$scope.doctor.last_name,phone_number:$scope.doctor.phone_number,city:$scope.doctor.city,area:$scope.doctor.area,experience_in_year:$scope.doctor.experience_in_year,education:$scope.doctor.education,email:$scope.doctor.email}
	    };
  		// doc = {first_name:$rootScope.first_name,last_name:$rootScope.last_name,phone_number:$rootScope.phone_number,city:$rootScope.city,area:$rootScope.area,experience_in_year:$rootScope.experience_in_year,education:$rootScope.education,email:$rootScope.email}
		console.log("Hello",req['data']);
		$http.post(q, req['data'])
        .success(function(data, status, headers, config){
          console.log(data);
      });
      $location.path('/');
  	}
})
.controller('EditClinicController', function($scope,$http,$location,$q,$rootScope){
	$scope.getClinic = function(){
		$rootScope.id = $scope.Id;
      $location.path('/editClinic');
  	}
  	$scope.EditClinic = function(){
  		var q = 'http://127.0.0.1:5000/add_clinic/'+String($rootScope.id);
  		var req = {
	      method: 'POST',
	      url: 'http://localhost:5000/clinic',
	      headers: {'Content-Type': 'application/json'},
	      data: {name: $scope.clinic.name, city:$scope.clinic.city,area:$scope.clinic.area,complete_address:$scope.clinic.complete_address ,timings:$scope.timing,fee:$scope.fee}
	    };
  		// doc = {first_name:$rootScope.first_name,last_name:$rootScope.last_name,phone_number:$rootScope.phone_number,city:$rootScope.city,area:$rootScope.area,experience_in_year:$rootScope.experience_in_year,education:$rootScope.education,email:$rootScope.email}
		// console.log("Hello",req['data']);
		$http.post(q, req['data'])
        .success(function(data, status, headers, config){
          // console.log(data);
      });
      $location.path('/');
  	}
})
.controller('SearchController', function($scope,$http,$location,$q,$rootScope){
	$scope.SearchName = function(){
		$rootScope.name = $scope.name;
		console.log($rootScope.name);
		var q = 'http://127.0.0.1:5000/search_name/'+String($rootScope.name);
		$http.get(q)
        .success(function(data, status, headers, config){
          $rootScope.doctors = data['results']
          console.log($rootScope.doctors);
      });
		$location.path('/SearchName');
	}

	$scope.SearchEmail = function(){
		$rootScope.email = $scope.email;
		console.log($rootScope.name);
		var q = 'http://127.0.0.1:5000/search_email/'+String($rootScope.email);
		$http.get(q)
        .success(function(data, status, headers, config){
          $rootScope.doctors = data['results']
          console.log($rootScope.doctors);
      });
		$location.path('/SearchName');
	}

	$scope.SearchCity = function(){
		$rootScope.city = $scope.city;
		console.log($rootScope.city);
		var q = 'http://127.0.0.1:5000/search_email/'+String($rootScope.city);
		$http.get(q)
        .success(function(data, status, headers, config){
          $rootScope.doctors = data['results']
          console.log($rootScope.doctors);
      });
		$location.path('/SearchName');
	}
})