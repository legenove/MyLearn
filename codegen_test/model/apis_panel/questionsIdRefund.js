/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdRefund = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 200    type:object
            return_code   'string' 返回状态码/SUCCESS/FAIL
            err_code_des   'string' 错误结果
            result_code   'string' 业务结果
            mch_id   'string' 商户号
            out_trade_no   'string' 商户系统内部的订单号
            return_msg   'string' 返回信息，如非空，为错误原因
            total_fee   'integer' 
            out_refund_no   'string' 商户退款单号
            transaction_id   'string' 微信订单号
            err_code   'string' 列表详见错误码列表
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/" + obj.id + "/refund",
            method: "PUT",
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
    QuestionsIdRefund: new QuestionsIdRefund
};