/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var SelfTalks = function () {
    /*
        @params obj 'data params'
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            listenings_count   'integer' 
            content   'ref' 
            reply_authors   'string' 
            date_created   'ref' 
            answers_count   'integer' 
            id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/self/talks",
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
    SelfTalks: new SelfTalks
};