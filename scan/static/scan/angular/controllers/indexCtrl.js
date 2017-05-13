(function(){
    scanApp.controller('indexCtrl', ['indexFactory', 'alertFactory', function(indexFactory, alertFactory){
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
            });
        }
        self.refresh = function(e){
            var target = e.currentTarget;
            target.classList.add('refresh-active');
            setTimeout(function(){
                target.classList.remove('refresh-active');
            }, 1000);
            alertFactory.add('refresh success');
            init();
        };
        self.addDanger = function(){
            alertFactory.add('Danger message dnanger', 'danger');
        };
        // init
        init();
    }])
}());