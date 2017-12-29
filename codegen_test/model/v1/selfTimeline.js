/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var SelfTimeline = function () {
    /*
        @params obj 'data params'
            question_id   'string' question id in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            free_type   'string' 
            listenings_count   'integer' 
            respondent_id   'ref' 
            respondent   'ref' 
            offer   'ref' 
            date_updated   'ref' 
            is_free_in_30mins   'boolean' 
            is_free   'boolean' 
            content   'ref' 
            remaining_seconds   'integer' 
            answer   'ref' 
            date_created   'ref' 
            type   'ref' 
            id   'ref' 
            visitor_count   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/self/timeline",
            method: "GET",
            data: {
                question_id: obj.question_id,
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
    SelfTimeline: new SelfTimeline
};