(function(){
    scanApp.controller('indexCtrl', ['indexFactory', function(indexFactory){
        var self = this;
        self.submit = function(){
            indexFactory.post(self.info).then(function(r){
                alert('Success');
                self.data.push(r.data.item);
            })
        };
        
        function init(){
            indexFactory.list().then(function(r){
                self.data = r.data.items;
            })
        }

        // init
        init();
    }])
}());