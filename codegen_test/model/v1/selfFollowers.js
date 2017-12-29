/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var SelfFollowers = function () {
    /*
        @params obj 'data params'
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            title   'ref' 
            is_verified   'boolean' 
            price   'integer' 
            avatar   'ref' 
            nickname   'string' 
            id   'ref' 
            answers_count   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/self/followers",
            method: "GET",
            data: {
                limit: obj.limit,
                offset: obj.offset,
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
    SelfFollowers: new SelfFollowers
};