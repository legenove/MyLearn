/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var RecommendAnswerers = function () {
    /*
        @params obj 'data params'
            kw   'string' key word in query
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:object
            wanted   'ref' 
            answerers   'array' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/recommend/answerers",
            method: "GET",
            data: {
                kw: obj.kw,
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
    RecommendAnswerers: new RecommendAnswerers
};