/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Respondents = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            nickname   'string' nickname in query
            is_star   'boolean' is star in query
            is_verified   'boolean' is verified in query
            category   'string' category in query
            span_with_answer   'integer' span in query
            span_with_visitor   'integer' span in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            public_answers_count   'integer' 
            order_score   'integer' 
            xanswers_count   'integer' 
            is_star   'boolean' 
            id   'ref' 
            xtopup_count   'integer' 
            x_visitor_count   'integer' 
            verify_category   'string' 
            income   'integer' 
            topup_income   'integer' 
            xlistenings_count   'integer' 
            nickname   'ref' 
            answers_count   'integer' 
            is_verified   'boolean' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/respondents",
            method: "GET",
            data: {
                id: obj.id,
                nickname: obj.nickname,
                is_star: obj.is_star,
                is_verified: obj.is_verified,
                category: obj.category,
                span_with_answer: obj.span_with_answer,
                span_with_visitor: obj.span_with_visitor,
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
    Respondents: new Respondents
};