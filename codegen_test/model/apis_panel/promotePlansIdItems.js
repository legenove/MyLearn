/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var PromotePlansIdItems = function () {
    /*
        @params obj 'data params'
            id   'integer' int id in query
            question_id   'string' question id in query
            respondent_id   'integer' respondent id in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            plan_id   'ref' 
            respondent_id   'ref' 
            content   'string' 
            valid   'ref' 
            factor   'string' 
            visitor_count   'integer' 
            id   'ref' 
            question_id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/promote_plans/" + obj.id + "/items",
            method: "GET",
            data: {
                question_id: obj.question_id,
                respondent_id: obj.respondent_id,
                page: obj.page,
                per_page: obj.per_page,
                offset: obj.offset,
                limit: obj.limit
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
    PromotePlansIdItems: new PromotePlansIdItems
};