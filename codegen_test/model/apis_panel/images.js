/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Images = function () {
    /*
        @params obj 'data params'
            target_id   'string' image target id in query
            target_type   'string' image target type in query
            offset   'integer' offset number
            limit   'integer' limit number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            url   'string' 
            review_status   'string' 
            target_id   'string' 
            target_type   'string' 
            _url   'string' 
            id   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/images",
            method: "GET",
            data: {
                target_id: obj.target_id,
                target_type: obj.target_type,
                offset: obj.offset,
                limit: obj.limit,
                page: obj.page,
                per_page: obj.per_page
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
    Images: new Images
};