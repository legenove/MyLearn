/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TagsIdAccounts = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            offset   'integer' offset number
            limit   'integer' limit number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            is_followed   'boolean' 
            followers_count   'integer' 
            has_answer_probability   'boolean' 
            answer_probability   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/tags/" + obj.id + "/accounts",
            method: "GET",
            data: {
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
    TagsIdAccounts: new TagsIdAccounts
};