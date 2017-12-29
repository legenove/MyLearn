/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var SelfDiscussions = function () {
    /*
        @params obj 'data params'
            role   'string' discussion account role in query
            offset   'integer' offset number
            limit   'integer' limit number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            status   'string' 
            account_id   'integer' 
            date_updated   'ref' 
            account_role   'string' 
            question   'ref' 
            content   'string' 
            date_created   'ref' 
            type   'string' 
            id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/self/discussions",
            method: "GET",
            data: {
                role: obj.role,
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
    SelfDiscussions: new SelfDiscussions
};