(function(){
    'use strict';

    scanApp.factory('indexFactory', function($http){
        var url = '/api/info/';
        return {
            list: function(){
                return $http.get(url);
            },
            post: function(data){
                return $http.post(url, data);
            },
            put: function(id, data){
                return $http.put(url + id, data);
            }
        }
    }).factory('alertFactory', ['$timeout', function($timeout){
        var LEVEL = {
            'info': 10,
            'success': 20,
            'warning': 30,
            'danger': 40
        };
        var id = 0;
        var obj = {
            messages: [],
            add: function(msg, level){
                level = level || 'info';
                var index = 'id_alert_' + id++;
                this.messages.push({msg: msg, level: level, id: index});
                if (LEVEL[level] < LEVEL.warning) {
                    $timeout(function(){
                        var a = angular.element('#' + index);
                        a.find('.close').trigger('click');
                    }, 2500);
                }
            },
            remove: function($event){
                var $div = $($event.currentTarget).parent();
                $div.removeClass('active');
                // after remove active class, it will do an animation in 1.3 seconds
                return $timeout(function(){
                    obj.messages.splice(obj.messages.findIndex(function(v){
                        return v.id===$div.attr('id');
                    }), 1)
                }, 1300); // This is the animation time in css
            }
        };
        return obj;
    }])
}());