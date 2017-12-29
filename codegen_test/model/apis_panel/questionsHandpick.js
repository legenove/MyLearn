/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsHandpick = function () {
    /*
        @params obj 'data params'
            is_active   'boolean' is active in query
            question_id   'string' question id in query
            operator_id   'integer' operator id in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            date_updated   'ref' 
            question   'ref' 
            is_active   'boolean' 
            operator   'ref' 
            date_created   'ref' 
            id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/handpick",
            method: "GET",
            data: {
                is_active: obj.is_active,
                question_id: obj.question_id,
                operator_id: obj.operator_id,
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
    QuestionsHandpick: new QuestionsHandpick
};