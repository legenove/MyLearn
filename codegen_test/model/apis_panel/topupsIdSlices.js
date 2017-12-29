/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TopupsIdSlices = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            status   'string' 
            topup_id   'ref' 
            date_executed   'ref' 
            delay   'integer' 
            date_created   'ref' 
            id   'ref' 
            visitor_count   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/topups/" + obj.id + "/slices",
            method: "GET",
            data: {
                page: obj.page,
                per_page: obj.per_page,
                offset: obj.offset,
                limit: obj.limit
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
    TopupsIdSlices: new TopupsIdSlices
};