/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var TalksIdReplies = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            is_digest   'boolean' is digest in query
            offset   'integer' offset number
            limit   'integer' limit number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            free_type   'string' 
            library_id   'string' 
            listenings_count   'integer' 
            respondent   'ref' 
            date_updated   'ref' 
            asker   'ref' 
            is_free   'boolean' 
            content   'ref' 
            recommendation   'string' 
            answer   'ref' 
            type   'ref' 
            id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/talks/" + obj.id + "/replies",
            method: "GET",
            data: {
                is_digest: obj.is_digest,
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
    
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 201    type:object
            free_type   'string' 
            library_id   'string' 
            listenings_count   'integer' 
            respondent   'ref' 
            date_updated   'ref' 
            asker   'ref' 
            is_free   'boolean' 
            content   'ref' 
            recommendation   'string' 
            answer   'ref' 
            type   'ref' 
            id   'ref' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/talks/" + obj.id + "/replies",
            method: "POST",
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
    TalksIdReplies: new TalksIdReplies
};