/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var ImagesId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            review_status   'string' 
            
        @success
            status 200    type:object
            url   'string' 
            review_status   'string' 
            target_id   'string' 
            target_type   'string' 
            _url   'string' 
            id   'integer' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/images/" + obj.id + "",
            method: "PUT",
            data: {
                review_status: obj.review_status
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
    ImagesId: new ImagesId
};