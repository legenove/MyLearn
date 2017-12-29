/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AccountsIdAlbums = function () {
    /*
        @params obj 'data params'
            id   'integer' account id in path
            offset   'integer' offset number
            limit   'integer' limit number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            album_type   'string' 专辑类型
            items_count   'integer' 
            description   'string' 专辑描述
            title   'string' 专辑名字
            image   'string' 专辑封面
            creator   'ref' 
            is_free   'boolean' 
            share_description   'string' 专辑分享文案
            is_show_showcase   'boolean' 
            is_show_title   'boolean' 
            id   'string' 
            icon   'string' 专辑icon
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/accounts/" + obj.id + "/albums",
            method: "GET",
            data: {
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
    AccountsIdAlbums: new AccountsIdAlbums
};