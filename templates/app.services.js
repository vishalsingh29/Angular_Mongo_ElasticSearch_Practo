angular.module('DoctorServices', [])
  .factory('GetDoctors', ['$http', function($http){
    return {
    getAllUsers: function() {
       return [
          { firstName: 'Jane', lastName: 'Doe', age: 29 },
          { firstName: 'John', lastName: 'Doe', age: 32 }
       ];
    }
 };
  }]);