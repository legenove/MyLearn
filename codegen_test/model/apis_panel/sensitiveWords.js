/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var SensitiveWords = function () {
    /*
        @params obj 'data params'
            word   'string' sensitive word in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            date_created   'ref' 
            is_search   'boolean' 
            word   'string' 
            id   'ref' 
            is_common   'boolean' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/sensitive_words",
            method: "GET",
            data: {
                word: obj.word,
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
    
    /*
        @params obj 'data params'
            is_search   'boolean' 
            word   'string' 
            is_common   'boolean' 
            
        @success
            status 201    type:object
            date_created   'ref' 
            is_search   'boolean' 
            word   'string' 
            id   'ref' 
            is_common   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/sensitive_words",
            method: "POST",
            data: {
                is_search: obj.is_search,
                word: obj.word,
                is_common: obj.is_common
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
    SensitiveWords: new SensitiveWords
};