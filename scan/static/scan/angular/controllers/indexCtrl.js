(function(){
    scanApp.controller('indexCtrl', ['indexFactory', 'alertFactory', '$interval',
        function(indexFactory, alertFactory, $interval){
        var self = this;
        self.TimeOutList = [];
        self.submit = function(){
            indexFactory.post(self.info).then(function(r){
                alertFactory.add('refresh success');
                init();
            }, function(){
                alertFactory.add('submit failed', 'danger');
            });
        };
        
        function init(){
            return indexFactory.list().then(function(r){
                self.data = r.data.items;

                if(self.data.some(function(v){return v.status !== 'ac'})) {
                    if (!self.Interval) {
                        console.log('add Interval');
                        self.Interval = $interval(init, 10000);
                    }
                } else {
                    self.Interval && clearInterval(self.Interval);
                    console.log('all active, clear interval');
                    self.Interval = false;
                }
            });
        }
        self.refresh = function(e){
            var target = e.currentTarget;
            target.classList.add('refresh-active');
            setTimeout(function(){
                target.classList.remove('refresh-active');
            }, 1000);
            init().then(function(){alertFactory.add('refresh success');});
        };
        // init
        init();
    }])
}());