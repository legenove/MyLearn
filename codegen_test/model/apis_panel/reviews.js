/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Reviews = function () {
    /*
        @params obj 'data params'
            target_id   'string' 
            target_type   'string' 
            
        @success
            status 200    type:object
            status   'string' 
            operator_id   'integer' 
            date_updated   'string' 
            target_id   'string' 
            target_type   'string' 
            date_created   'string' 
            id   'integer' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/reviews",
            method: "POST",
            data: {
                target_id: obj.target_id,
                target_type: obj.target_type
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    Reviews: new Reviews
};