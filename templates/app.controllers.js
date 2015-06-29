angular.module('DoctorControllers',[])
  .controller('DoctorController', ['$scope', 'GetDoctors', function($scope, GetDoctors){
    console.log("Hello")
    $scope.users = userRepository.getAllUsers();
    console.log($scope.users);
  }]);