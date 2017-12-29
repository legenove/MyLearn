/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Talks = function () {
    /*
        @params obj 'data params'
            library_id   'string' question library id in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            listenings_count   'integer' 
            description   'string' 
            is_sticky   'boolean' 
            introduction   'string' 
            image   'string' 
            date_updated   'ref' 
            share_description   'string' 
            share_title   'string' 
            is_hot   'boolean' 
            answers_count   'integer' 
            guide   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/talks",
            method: "GET",
            data: {
                library_id: obj.library_id,
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
    Talks: new Talks
};