(function(){
    'use strict';
    
    angular.module('scanApp').controller('alertCtrl', alertCtrl);
    
    alertCtrl.$inject = ['alertFactory', '$scope'];
    
    function alertCtrl (alertFactory, $scope) {
        var self = this;
        self.messages = alertFactory.messages;
        self.remove = function(e, i) {
            alertFactory.remove(e, i);
        }
    }
}());