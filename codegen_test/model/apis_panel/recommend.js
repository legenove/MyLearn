/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Recommend = function () {
    /*
        @params obj 'data params'
            question_id   'string' question id in query
            respondent_id   'integer' respondent id in query
            status   'string' status in query
            order_by   'string' order by in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            status   'string' 
            listenings_count   'integer' 
            respondent   'ref' 
            true_visitor_count   'integer' 
            question_content   'ref' 
            question_offer   'ref' 
            question_asker   'ref' 
            countdown   'integer' 
            likings_count   'integer' 
            position   'integer' 
            date_created   'ref' 
            question_id   'ref' 
            id   'ref' 
            visitor_count   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/recommend",
            method: "GET",
            data: {
                question_id: obj.question_id,
                respondent_id: obj.respondent_id,
                status: obj.status,
                order_by: obj.order_by,
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
            question_id   'string' 
            
        @success
            status 201    type:object
            status   'string' 
            listenings_count   'integer' 
            respondent   'ref' 
            true_visitor_count   'integer' 
            question_content   'ref' 
            question_offer   'ref' 
            question_asker   'ref' 
            countdown   'integer' 
            likings_count   'integer' 
            position   'integer' 
            date_created   'ref' 
            question_id   'ref' 
            id   'ref' 
            visitor_count   'integer' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/recommend",
            method: "POST",
            data: {
                question_id: obj.question_id
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
    Recommend: new Recommend
};