/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var ReportsQuestion = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            question_id   'string' question id in query
            operator_id   'integer' operator id in query
            status   'string' 举报状态
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            question   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/reports/question",
            method: "GET",
            data: {
                account_id: obj.account_id,
                question_id: obj.question_id,
                operator_id: obj.operator_id,
                status: obj.status || "pending",
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
    ReportsQuestion: new ReportsQuestion
};